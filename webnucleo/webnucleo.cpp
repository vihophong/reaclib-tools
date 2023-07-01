#include "webnucleo.h"
#include <fstream>
#include <sstream>
#include <stdio.h>
#define NUCLIDE_PARTITION_FUNCTION_T9                                           \
    0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,                              \
    1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

#define NumPartitionFunctionEntries 24


void WebnucleoXml::Init()
{
    XMLdoc = new tinyxml2::XMLDocument;
    XMLdoc->LoadFile(finputXML);
    int k=0;
    for (tinyxml2::XMLNode* node = XMLdoc->RootElement()->FirstChildElement("nuclide"); node != nullptr;
         node = node->NextSiblingElement("nuclide")){
        ReadNuclide(node);
        k++;
    }
}


void WebnucleoXml::UpdateData(char *inputCSV,char* outputXML)
{

    std::vector<std::vector<std::string>> content;
    std::vector<std::string> row;
    std::string line, word;

    std::fstream file (inputCSV, std::ios::in);
    if(file.is_open())
    {
        while(getline(file, line))
        {
            row.clear();

            std::stringstream str(line);

            while(getline(str, word, ','))
                row.push_back(word);
            content.push_back(row);
        }
    }
    else
        std::cout<<"Could not open the file\n";

    for(int i=0;i<content.size();i++)//rows
    {
        for(int j=0;j<content[i].size();j++)//cols
        {
            std::cout<<content[i][j]<<" ";
        }
        std::cout<<"\n";
    }

    bool is_update[4];for (int i=0;i<4;i++) is_update[i]=false;
    std::string update_name[] = {"spin","mass","source","partFcn"};

    std::vector<int> myA;
    std::vector<int> myZ;
    std::vector<double> myspin;
    std::vector<std::string> mysource;
    std::vector<double> mymass_excess;
    std::vector<std::vector<double>> mypartFuncLog10;

    for(int j=2;j<content[0].size();j++)//cols
    {
        for (int k=0;k<4;k++){
            if (content[0][j]==update_name[k]){
                is_update[k] = true;
            }
        }
    }

    for(int i=1;i<content.size();i++)//rows
    {
        myZ.push_back(std::stoi(content[i][0]));
        myA.push_back(std::stoi(content[i][1]));
        std::vector<double> mypartFuncLog10items;
        for(int j=2;j<content[i].size();j++)//cols
        {
            if (content[0][j]=="spin")
                myspin.push_back(std::stod(content[i][j]));
            if (content[0][j]=="mass_excess")
                mymass_excess.push_back(std::stod(content[i][j]));
            if (content[0][j]=="source")
                mysource.push_back(content[i][j]);
            if (content[0][j]=="partFuncLog10")
                mypartFuncLog10items.push_back(std::stod(content[i][j]));
        }
        if (mypartFuncLog10items.size()>0)
            mypartFuncLog10.push_back(mypartFuncLog10items);
    }


    for (tinyxml2::XMLNode* node = XMLdoc->RootElement()->FirstChildElement("nuclide"); node != nullptr;
         node = node->NextSiblingElement("nuclide")){
        // read Z
        auto pZ = node->FirstChildElement("z");
        if (!pZ)
            throw std::invalid_argument("No z element");
        int z = std::stoi(pZ->GetText());
        // read A
        auto pA = node->FirstChildElement("a");
        if (!pA)
            throw std::invalid_argument("No a element");
        int a = std::stoi(pA->GetText());

        if (mysource.size()>0){
            // write source
            auto pSource = node->FirstChildElement("source");
            if (!pSource)
                throw std::invalid_argument("No source element");
            for (int i=0;i<myA.size();i++){
                if (myA[i]==a && myZ[i]==z){
                    pSource->SetText(mysource[i].c_str());
                }
            }
        }


        if (mymass_excess.size()>0){
            // write mass excess
            auto pMassExcess = node->FirstChildElement("mass_excess");
            if (!pMassExcess)
                throw std::invalid_argument("No mass_excess element");

            for (int i=0;i<myA.size();i++){
                if (myA[i]==a && myZ[i]==z){
                    char tmpchr[500];
                    sprintf(tmpchr,"%g",mymass_excess[i]);
                    pMassExcess->SetText(tmpchr);
                }
            }
        }

        if (myspin.size()>0){
            // write spin
            auto pSpin = node->FirstChildElement("spin");
            if (!pSpin)
                throw std::invalid_argument("No spin element");

            for (int i=0;i<myA.size();i++){
                if (myA[i]==a && myZ[i]==z){
                    char tmpchr[500];
                    sprintf(tmpchr,"%g",myspin[i]);
                    pSpin->SetText(tmpchr);
                }
            }
        }

        // read partition function
        unsigned int counter = 0;
        std::array<double, NumPartitionFunctionEntries> partfLog10;

        auto pPartfTable = node->FirstChildElement("partf_table");
        if (!pPartfTable)
            throw std::invalid_argument("No partf_table element");
        // loop over points

        std::vector<double> t9vec;
        std::vector<double> log10vec;

        if (mypartFuncLog10.size()>0){
            int pointid = 0;
            int myindex = -1;
            for (int i=0;i<myA.size();i++){
                if (myA[i]==a && myZ[i]==z){
                    myindex = i;
                }
            }

            for (auto point = pPartfTable->FirstChildElement("point"); point != nullptr;
                 point = point->NextSiblingElement("point")) {
                auto pT9 = point->FirstChildElement("t9");
                if (!pT9)
                    throw std::invalid_argument("No t9 element");
                double t9 = std::stod(pT9->GetText());

                auto pLog10 = point->FirstChildElement("log10_partf");
                if (!pLog10)
                    throw std::invalid_argument("No log10_partf element");

                if (myindex>=0 && pointid<mypartFuncLog10[myindex].size()){
                    char tmpchr[500];
                    sprintf(tmpchr,"%g",mypartFuncLog10[myindex][pointid]);
                    pLog10->SetText(tmpchr);
                }

                double log10 = std::stod(pLog10->GetText());

                double PartitionFunctionT9[24] = {
                    NUCLIDE_PARTITION_FUNCTION_T9
                };

                // check T9 is as expected
                if (t9 != PartitionFunctionT9[counter])
                    throw std::invalid_argument("Unexpected value for T9 in partition "
                                                "function");

                if (counter >= NumPartitionFunctionEntries)
                    throw std::invalid_argument("Too many partition function entries");

                partfLog10[counter++] = log10;
                t9vec.push_back(t9);
                log10vec.push_back(log10);

                pointid++;
            }

            if (counter != NumPartitionFunctionEntries) {
                throw std::invalid_argument("Wrong number of partition function entries");
            }
        }
    }


    XMLdoc->SaveFile(outputXML);
}

void WebnucleoXml::ReadNuclide(tinyxml2::XMLNode* node){
    // read Z
    auto pZ = node->FirstChildElement("z");
    if (!pZ)
        throw std::invalid_argument("No z element");
    int z = std::stoi(pZ->GetText());

    // read A
    auto pA = node->FirstChildElement("a");
    if (!pA)
        throw std::invalid_argument("No a element");
    int a = std::stoi(pA->GetText());

    // read source
    auto pSource = node->FirstChildElement("source");
    if (!pSource)
        throw std::invalid_argument("No source element");
    std::string source = pSource->GetText();

    // read mass excess
    auto pMassExcess = node->FirstChildElement("mass_excess");
    if (!pMassExcess)
        throw std::invalid_argument("No mass_excess element");
    double massExcess = std::stod(pMassExcess->GetText());

    // read spin
    auto pSpin = node->FirstChildElement("spin");
    if (!pSpin)
        throw std::invalid_argument("No spin element");
    double spin = std::stod(pSpin->GetText());

    // read partition function
    unsigned int counter = 0;
    std::array<double, NumPartitionFunctionEntries> partfLog10;

    auto pPartfTable = node->FirstChildElement("partf_table");
    if (!pPartfTable)
        throw std::invalid_argument("No partf_table element");
    // loop over points

    std::vector<double> t9vec;
    std::vector<double> log10vec;

    for (auto point = pPartfTable->FirstChildElement("point"); point != nullptr;
         point = point->NextSiblingElement("point")) {
        auto pT9 = point->FirstChildElement("t9");
        if (!pT9)
            throw std::invalid_argument("No t9 element");
        double t9 = std::stod(pT9->GetText());

        auto pLog10 = point->FirstChildElement("log10_partf");
        if (!pLog10)
            throw std::invalid_argument("No log10_partf element");
        double log10 = std::stod(pLog10->GetText());

        double PartitionFunctionT9[24] = {
            NUCLIDE_PARTITION_FUNCTION_T9
        };

        // check T9 is as expected
        if (t9 != PartitionFunctionT9[counter])
            throw std::invalid_argument("Unexpected value for T9 in partition "
                                        "function");

        if (counter >= NumPartitionFunctionEntries)
            throw std::invalid_argument("Too many partition function entries");

        partfLog10[counter++] = log10;
        t9vec.push_back(t9);
        log10vec.push_back(log10);
    }

    if (counter != NumPartitionFunctionEntries) {
        throw std::invalid_argument("Wrong number of partition function entries");
    }
    fZ.push_back(z);
    fA.push_back(a);
    fspin.push_back(spin);
    fsource.push_back(source);
    fmass_excess.push_back(massExcess);
    fpartFuncT9.push_back(t9vec);
    fpartFuncLog10.push_back(log10vec);
    fZA[z][a] = true;
}
