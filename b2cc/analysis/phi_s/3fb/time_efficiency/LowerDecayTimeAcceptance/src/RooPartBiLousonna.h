/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef ROOPARTBILOUSONNA
#define ROOPARTBILOUSONNA

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"
 
class RooPartBiLousonna : public RooAbsPdf {
public:
  RooPartBiLousonna() {} ; 
  RooPartBiLousonna(const char *name, const char *title,
                    RooAbsReal& _m,
                    RooAbsReal& _m0,
                    RooAbsReal& _sigma,
                    RooAbsReal& _nu,
                    RooAbsReal& _alpha_l,
                    RooAbsReal& _n_l,
                    RooAbsReal& _alpha_r,
                    RooAbsReal& _n_r);
  RooPartBiLousonna(const RooPartBiLousonna& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new RooPartBiLousonna(*this,newname); }
  inline virtual ~RooPartBiLousonna() { }

protected:

  RooRealProxy m ;
  RooRealProxy m0 ;
  RooRealProxy sigma ;
  RooRealProxy nu ;
  RooRealProxy alpha_l ;
  RooRealProxy n_l ;
  RooRealProxy alpha_r ;
  RooRealProxy n_r ;
  
  Double_t evaluate() const ;
  //Int_t getAnalyticalIntegral( RooArgSet& allVars,  RooArgSet& analVars, const char* rangeName=0 ) const;
  //Double_t analyticalIntegral( Int_t code, const char* rangeName=0 ) const;
  
private:

  //ClassDef(RooPartBiLousonna,1) // Your description goes here...
};
 
#endif
