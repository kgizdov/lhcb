 /***************************************************************************** 
  * Project: RooFit                                                           * 
  *                                                                           * 
  * This code was autogenerated by RooClassFactory                            * 
  *****************************************************************************/ 

 // Your description goes here... 

 #include "Riostream.h" 

 #include "RooStudentT.h" 
 #include "RooAbsReal.h" 
 #include "RooAbsCategory.h" 
 #include <math.h> 
 #include "TMath.h" 

//ClassImp(RooStudentT) 

 RooStudentT::RooStudentT(const char *name, const char *title, 
                        RooAbsReal& _m,
                        RooAbsReal& _m0,
                        RooAbsReal& _sigma,
                        RooAbsReal& _nu) :
   RooAbsPdf(name,title), 
   m("m","m",this,_m),
   m0("m0","m0",this,_m0),
   sigma("sigma","sigma",this,_sigma),
   nu("nu","nu",this,_nu)
 { 
 } 


 RooStudentT::RooStudentT(const RooStudentT& other, const char* name) :  
   RooAbsPdf(other,name), 
   m("m",this,other.m),
   m0("m0",this,other.m0),
   sigma("sigma",this,other.sigma),
   nu("nu",this,other.nu)
 { 
 } 


 Double_t RooStudentT::evaluate() const 
 { 
   return TMath::Student((m-m0)/sigma,nu);
 } 

 Int_t RooStudentT::getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName) const
 {
   if( matchArgs(allVars,analVars,m) )
     return 1 ;
   
   return 0;
 }


 Double_t RooStudentT::analyticalIntegral(Int_t code, const char* rangeName) const
 {
   assert(code==1);

   double tmin = (m.min(rangeName)-m0)/sigma;
   double tmax = (m.max(rangeName)-m0)/sigma;
   
   return sigma*(TMath::StudentI(tmax,nu) - TMath::StudentI(tmin,nu));
 }

 Int_t RooStudentT::getMaxVal(const RooArgSet& vars) const 
 {
   RooArgSet dummy ;
   
   if (matchArgs(vars,dummy,m)) {
     return 1 ;
   }
   return 0 ;
 }


 Double_t RooStudentT::maxVal(Int_t code) const
 { 
   assert(code==1) ;
   
   return 1.0 ;
 }

