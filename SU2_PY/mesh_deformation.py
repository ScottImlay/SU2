#!/usr/bin/env python 

## \file mesh_deformation.py
#  \brief Python script for doing the parallel deformation using SU2_DEF.
#  \author F. Palacios
#  \version 6.1.0 "Falcon"
#
# The current SU2 release has been coordinated by the
# SU2 International Developers Society <www.su2devsociety.org>
# with selected contributions from the open-source community.
#
# The main research teams contributing to the current release are:
#  - Prof. Juan J. Alonso's group at Stanford University.
#  - Prof. Piero Colonna's group at Delft University of Technology.
#  - Prof. Nicolas R. Gauger's group at Kaiserslautern University of Technology.
#  - Prof. Alberto Guardone's group at Polytechnic University of Milan.
#  - Prof. Rafael Palacios' group at Imperial College London.
#  - Prof. Vincent Terrapon's group at the University of Liege.
#  - Prof. Edwin van der Weide's group at the University of Twente.
#  - Lab. of New Concepts in Aeronautics at Tech. Institute of Aeronautics.
#
# Copyright 2012-2018, Francisco D. Palacios, Thomas D. Economon,
#                      Tim Albring, and the SU2 contributors.
#
# SU2 is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# SU2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SU2. If not, see <http://www.gnu.org/licenses/>.

import os, sys
from optparse import OptionParser
sys.path.append(os.environ['SU2_RUN'])
import SU2

# -------------------------------------------------------------------
#  Main 
# -------------------------------------------------------------------

def main():
    
    # Command Line Options
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read config from FILE", metavar="FILE")
    parser.add_option("-n", "--partitions", dest="partitions", default=2,
                      help="number of PARTITIONS", metavar="PARTITIONS")

    (options, args)=parser.parse_args()
    options.partitions = int( options.partitions )
    
    # Run Parallel Comutation
    mesh_deformation ( options.filename    ,
                       options.partitions   )
#: def main()

  
# -------------------------------------------------------------------
#  Parallel Computation Function
# -------------------------------------------------------------------

def mesh_deformation( filename           ,
                      partitions  = 2     ):
    
    # Config
    config = SU2.io.Config(filename)
    config.NUMBER_PART = partitions
    config.DV_VALUE_NEW = config.DV_VALUE
    
    # State
    state = SU2.io.State()
    
    state.FILES.MESH = config.MESH_FILENAME

    # Deformation
    info = SU2.run.DEF(config)
    state.update(info)
    
    return state

#: mesh_deformation()


# -------------------------------------------------------------------
#  Run Main Program
# -------------------------------------------------------------------

# this is only accessed if running from command prompt
if __name__ == '__main__':
    main()
    
    
