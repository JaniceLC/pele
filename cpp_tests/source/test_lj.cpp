#include "pele/array.h"
#include "pele/lj.h"
#include "pele/lj_cut.h"

#include <iostream>
#include <stdexcept>
#include <vector>
#include <gtest/gtest.h>
#include <cmath>
#include <memory>

using pele::Array;


TEST(LJInteractionTest, Energy_Works){
    double r2 = 1.1;
    double c6 = 1.2;
    double c12 = 2.3;
    pele::lj_interaction ljint(c6, c12);
    ASSERT_NEAR(ljint.energy(r2, 1, 2), 0.39671227804179443, 1e-10);
}

TEST(LJInteractionTest, EnergyGradient_Works){
    double r2 = 1.1;
    double c6 = 1.2;
    double c12 = 2.3;
    pele::lj_interaction ljint(c6, c12);
    double g = 0;
    double e = ljint.energy_gradient(r2, &g, 1, 2);
    ASSERT_NEAR(e, 0.39671227804179443, 1e-10);
    ASSERT_NEAR(g, 9.2454671845389917, 1e-10);
}

TEST(LJInteractionTest, Hessian_Works){
    double r2 = 1.1;
    double c6 = 1.2;
    double c12 = 2.3;
    pele::lj_interaction ljint(c6, c12);
    double h = 0, g = 0;
    double e = ljint.energy_gradient_hessian(r2, &g, &h, 1, 2);
    ASSERT_NEAR(e, 0.39671227804179443, 1e-10);
    ASSERT_NEAR(g, 9.2454671845389917, 1e-10);
    ASSERT_NEAR(h, 149.6972546707778, 1e-10);
}

class PotentialTest :  public ::testing::Test
{
public:
    std::shared_ptr<pele::BasePotential> pot;
    double etrue;
    Array<double> x, g, gnum, h, hnum;

    void test_energy(){
        double e = pot->get_energy(x);
        ASSERT_NEAR(e, etrue, 1e-10);
    }

    void test_energy_gradient(){
        g.resize(x.size());
        gnum.resize(g.size());
        double e = pot->get_energy_gradient(x, g);
        EXPECT_NEAR(e, etrue, 1e-10);
        pot->numerical_gradient(x, gnum, 1e-6);
        for (size_t k=0; k<6; ++k){
            EXPECT_NEAR(g[k], gnum[k], 1e-6);
        }
    }

    void test_energy_gradient_hessian(){
        g.resize(x.size());
        gnum.resize(g.size());
        h.resize(x.size()*x.size());
        hnum.resize(h.size());
        double e = pot->get_energy_gradient_hessian(x, g, h);
        double ecomp = pot->get_energy(x);
        pot->numerical_gradient(x, gnum);
        pot->numerical_hessian(x, hnum);

        EXPECT_NEAR(e, ecomp, 1e-10);
        for (size_t i=0; i<g.size(); ++i){
            ASSERT_NEAR(g[i], gnum[i], 1e-6);
        }
        for (size_t i=0; i<h.size(); ++i){
            ASSERT_NEAR(h[i], hnum[i], 1e-3);
        }
    }
};

class LJTest :  public PotentialTest
{
public:

    double c6, c12;
    size_t natoms;

    virtual void setup_potential(){
        pot = std::shared_ptr<pele::BasePotential> (new pele::LJ(c6, c12));
    }

    virtual void SetUp(){
        natoms = 2;
        c6 = 1.2;
        c12 = 2.3;
        x.resize(3*natoms);
        x[0]  = 0.1;
        x[1]  = 0.2;
        x[2]  = 0.3;
        x[3]  = 0.44;
        x[4]  = 0.55;
        x[5]  = 1.66;
        etrue = -0.10410023149146598;

//        y = Array<double>(9);
//        for(size_t i=0;i<6;++i)
//            y[i] = x[i];
//        y[6] = 0.88;
//        y[7] = 1.1;
//        y[8] = 3.32;

        setup_potential();
    }


};

TEST_F(LJTest, Energy_Works){
    test_energy();
}

TEST_F(LJTest, EnergyGradient_AgreesWithNumerical){
    test_energy_gradient();
}

TEST_F(LJTest, EnergyGradientHessian_AgreesWithNumerical){
    test_energy_gradient_hessian();
}


/*
 * LJCut
 */

class LJCutTest :  public PotentialTest
{
public:
    double c6, c12, rcut;
    Array<double> y;
    virtual void SetUp(){
        c6 = 1.2;
        c12 = 2.3;
        rcut = 2.5;
        x = Array<double>(6);
        x[0]  = 0.1;
        x[1]  = 0.2;
        x[2]  = 0.3;
        x[3]  = 0.44;
        x[4]  = 0.55;
        x[5]  = 1.66;
        etrue = -0.089557709975460198;
        y = Array<double>(9);
        for(size_t i=0;i<6;++i)
            y[i] = x[i];
        y[6] = 0.88;
        y[7] = 1.1;
        y[8] = 3.32;

        pot = std::shared_ptr<pele::BasePotential> (new pele::LJCut(c6, c12, rcut));

    }
};

TEST_F(LJCutTest, Energy_Works){
    test_energy();
}

TEST_F(LJCutTest, EnergyGradient_AgreesWithNumerical){
    test_energy_gradient();
}

TEST_F(LJCutTest, EnergyGradientHessian_AgreesWithNumerical){
    test_energy_gradient_hessian();
}

TEST_F(LJCutTest, Hessian_Works2){
    pele::LJCut pot(c6, c12, rcut);
    Array<double> h(9*9);
    Array<double> h_num(9*9);
    pot.get_hessian(y, h);
    pot.numerical_hessian(y, h_num);
    for (size_t i=0; i<h.size();++i)
        ASSERT_NEAR(h[i],h_num[i],1e-6);
}

/*
 * LJNeighborList tests
 */

class LJNeighborListTest :  public LJTest
{
    virtual void setup_potential(){
        pele::Array<long> ilist(size_t(natoms*(natoms - 1)));
        size_t k = 0;
        for (size_t i=0; i < natoms; ++i){
            for (size_t j=0; j<i; ++j){
                ilist[k] = i;
                ilist[k+1] = j;
                k += 2;
            }
        }
        pot = std::shared_ptr<pele::BasePotential> (new pele::LJNeighborList(ilist, c6, c12));
    }
};

TEST_F(LJNeighborListTest, Energy_Works){
    test_energy();
}

TEST_F(LJNeighborListTest, EnergyGradient_AgreesWithNumerical){
    test_energy_gradient();
}

TEST_F(LJNeighborListTest, EnergyGradientHessian_AgreesWithNumerical){
    test_energy_gradient_hessian();
}

