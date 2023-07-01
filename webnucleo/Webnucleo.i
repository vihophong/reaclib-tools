%module Webnucleo
%include <carrays.i>
%include <exception.i>
%include <std_map.i>
%include <std_string.i>
%include <std_vector.i>
%include <std_shared_ptr.i>

%{
#include "webnucleo.h"
%}

%include "webnucleo.h"

%template(std_vector_int) std::vector<int>;
%template(std_vector_double) std::vector<double>;
%template(std_vector_std_vector_double) std::vector<std::vector<double>>;
%template(std_vector_std_string) std::vector<std::string>;
