# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /data03/users/phong/bin/cmake-3.20.1-linux-x86_64/bin/cmake

# The command to remove a file.
RM = /data03/users/phong/bin/cmake-3.20.1-linux-x86_64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build

# Utility rule file for Webnucleo_swig_compilation.

# Include any custom commands dependencies for this target.
include CMakeFiles/Webnucleo_swig_compilation.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Webnucleo_swig_compilation.dir/progress.make

CMakeFiles/Webnucleo_swig_compilation: CMakeFiles/Webnucleo.dir/WebnucleoPYTHON.stamp

CMakeFiles/Webnucleo.dir/WebnucleoPYTHON.stamp: ../Webnucleo.i
CMakeFiles/Webnucleo.dir/WebnucleoPYTHON.stamp: ../Webnucleo.i
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Swig compile Webnucleo.i for python"
	/data03/users/phong/bin/cmake-3.20.1-linux-x86_64/bin/cmake -E make_directory /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build/CMakeFiles/Webnucleo.dir
	/data03/users/phong/bin/cmake-3.20.1-linux-x86_64/bin/cmake -E touch /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build/CMakeFiles/Webnucleo.dir/WebnucleoPYTHON.stamp
	/data03/users/phong/bin/cmake-3.20.1-linux-x86_64/bin/cmake -E env SWIG_LIB=/home/phong/softwares/skynet2/swig-4.0.2-install/share/swig/4.0.2 /home/phong/softwares/skynet2/swig-4.0.2-install/bin/swig -python -outdir /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build -c++ -interface _Webnucleo -I/home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo -I/usr/include/python3.6m -o /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build/CMakeFiles/Webnucleo.dir/WebnucleoPYTHON_wrap.cxx /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/Webnucleo.i

Webnucleo_swig_compilation: CMakeFiles/Webnucleo.dir/WebnucleoPYTHON.stamp
Webnucleo_swig_compilation: CMakeFiles/Webnucleo_swig_compilation
Webnucleo_swig_compilation: CMakeFiles/Webnucleo_swig_compilation.dir/build.make
.PHONY : Webnucleo_swig_compilation

# Rule to build all files generated by this target.
CMakeFiles/Webnucleo_swig_compilation.dir/build: Webnucleo_swig_compilation
.PHONY : CMakeFiles/Webnucleo_swig_compilation.dir/build

CMakeFiles/Webnucleo_swig_compilation.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Webnucleo_swig_compilation.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Webnucleo_swig_compilation.dir/clean

CMakeFiles/Webnucleo_swig_compilation.dir/depend:
	cd /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build /home/phong/projects/update_reaclib_230628/reaclib-tools/webnucleo/build/CMakeFiles/Webnucleo_swig_compilation.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Webnucleo_swig_compilation.dir/depend
