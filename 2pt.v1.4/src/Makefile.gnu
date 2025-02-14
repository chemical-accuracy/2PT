# RedHat Linux 64 bit machine, Intel icpc 64 bit version 11.1, FFTW 3.2.2

SHELL = /bin/sh

# ---------------------------------------------------------------------
# compiler/linker settings
# edit this section if additional compiler/linker flags or 
# libraries are needed for your machine

CC = g++
FFTW = /usr/local/
#CDEBUG= -g -Wall -DDEBUG=1
CDEBUG= -DDEBUG=0
OPTFLAGS = -O3 -I${FFTW}/include
LIBFLAGS = ${FFTW}/lib/libfftw3.a -lm -lstdc++ -static

# generally no need to edit the following sections

# Compile file list

OBJS = analysis.o  compute_vac.o  control.o  driver.o  model.o  memory.o statistics.o \
	structure.o  timing.o  trajectory.o  trj_header.o trj_reader.o utility.o 

# Link target

2pt_analysis :${OBJS}
	${CC} ${OPTFLAGS} -o $@ ${OBJS}  ${LIBFLAGS}

# Compilation rules

%.o : %.cpp
	${CC} ${OPTFLAGS} ${CDEBUG} -o $@ -c $< 

# Make options
clean:
	@rm -f *.o out core *.out 2pt_analysis

install:
	@mkdir -p ../bin
	@make
	@mv 2pt_analysis ../bin/
