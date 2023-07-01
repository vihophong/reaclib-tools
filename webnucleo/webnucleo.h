#pragma once

#include <iostream>
#include <fstream>
#include <array>
#include <string>
#include <stdio.h>

#include "tinyxml2.h"

#include <vector>

class WebnucleoXml {
public:
     WebnucleoXml(char* inp){
         for (int i=0;i<150;i++){
             for (int j=0;j<500;j++){
                 fZA[i][j] = false;
             }
         }
        SetInputFile(inp);
        Init();
    }
    WebnucleoXml(){}

    void SetInputFile(char* inp){finputXML = inp;}
    void Init();

    void UpdateData(char* inputCSV, char *outputXML);

    const std::vector<int>& Z() const {
      return fZ;
    }
    const std::vector<int>& A() const {
      return fA;
    }

    const std::vector<double>& Spin() const {
      return fspin;
    }

    const std::vector<double>& Mass_excess() const {
      return fmass_excess;
    }


    const std::vector<std::string>& Source() const {
      return fsource;
    }

    const std::vector<std::vector<double>>& PartFuncT9() const{
        return fpartFuncT9;
    }
    const std::vector<std::vector<double>>& PartFuncLog10() const{
        return fpartFuncLog10;
    }

private:
  // don't allow this class to be constructed
  char* finputXML;
  tinyxml2::XMLDocument* XMLdoc;
  void ReadNuclide(tinyxml2::XMLNode* node);

  std::vector<int> fA;
  std::vector<int> fZ;
  std::vector<double> fspin;
  std::vector<std::string> fsource;
  std::vector<double> fmass_excess;
  std::vector<std::vector<double>> fpartFuncT9;
  std::vector<std::vector<double>> fpartFuncLog10;

  bool fZA[150][500];

};
