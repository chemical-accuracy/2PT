import readline
import numpy as np
import argparse

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description='convert the LAMMPS trajectory file to xyz')
parser.add_argument('folder', type=str)
parser.add_argument('file_in', type=str)
parser.add_argument('file_out', type=str)
args = parser.parse_args()
folder, file_to_open, file_to_write = args.folder, args.file_in, args.file_out
with open(folder+file_to_open,'r') as in_file:
    with open(folder+file_to_write+'vel.xyz','w') as vel_file:
        with open(folder+file_to_write+'pos.xyz','w') as pos_file:
            for iii in range(10000):
                #Get the timestep
                line = in_file.readline()
                while("TIMESTEP" not in line):
                    line = in_file.readline()
                Step = int(in_file.readline())
                #Get the number of atoms
                line = in_file.readline()
                while("NUMBER OF ATOMS" not in line):
                    line = in_file.readline()
                Natoms = int(in_file.readline())

                #Get positions and velocities
                line = in_file.readline()
                while("ATOMS" not in line):
                    line = in_file.readline()
                # line = in_file.readline()
                velocities=np.empty((Natoms,3))
                positions=np.empty((Natoms,3))
                for i in range(Natoms):
                    line = in_file.readline().split()
                    positions[int(line[0])-1,:] = [float(line[ii]) for ii in range(2,5)]
                    velocities[int(line[0])-1,:] = [float(line[ii]) for ii in range(5,8)]
                vel_file.write(f"{Natoms}\n")
                vel_file.write(f"STEP {Step}\n")
                pos_file.write(f"{Natoms}\n")
                pos_file.write(f"STEP {Step}\n")
                for i in range(Natoms): # atoms
                    atom = 'O'*(not bool(i%3)) + 'H'*bool(i%3)
                    pos_file.write(f"{atom}\t\t"+ '\t\t'.join(map(str,positions[i,:])) + "\n")
                    vel_file.write(f"{atom}\t\t"+ "\t\t".join(map(str,velocities[i,:]))+ "\n")
                            