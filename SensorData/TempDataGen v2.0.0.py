
#===================================#
# Temperature Sensor Data Generator #
#   ECE2195 Project - Team Two      #
#   v2.0.0                          #
#===================================#


# Imports
import math;
import random;


# Variable Initialization
filename = "file";
length   = 500;
pattern  = 1;
minTemp  = 0;
maxTemp  = 100;
tempSAF  = 0;
SAFValue = 0;
SAFStart = 0;
SAFEnd   = 0;
noise    = 0;
noiseMax = 0;
v_max    = 3.3;


# Evaluation Functions

def linFall( dif, size, n, maximum ):
  return ( ( -dif / size ) * n ) + maximum;

def linRise( dif, size, n, minimum ):
  return ( ( dif / size ) * n ) + minimum;

def fall( dif, size, n, minimum ):
  return ( dif / 2 ) * math.cos( ( math.pi / size ) * n ) + ( minimum + ( dif / 2 ) );

def rise( dif, size, n, minimum ):
  return ( dif / 2 ) * math.cos( ( math.pi / size ) * ( n + size ) ) + ( minimum + ( dif / 2 ) );

def dip( dif, size, n, minimum ):
  return ( dif / 2 ) * math.cos( ( ( 2 * math.pi ) / size ) * n ) + ( minimum + ( dif / 2 ) );

def hump( dif, size, n, minimum ):
  return ( dif / 2 ) * math.cos( ( ( 2 * math.pi ) / size ) * ( n + ( size / 2 ) ) ) + ( minimum + ( dif / 2 ) );


# Start Display
print( "\n\n===================================\n Temperature Sensor Data Generator \n===================================\n\n" );

# Gathering Input
filename      =        input( " Enter a Filename:              " );
length        = int(   input( " Number of Data Points:         " ) );
print( " Data Patterns\n  (1) Linear Fall\n  (2) Linear Rise\n  (3) Sine Fall\n  (4) Sine Rise\n  (5) Sine Dip\n  (6) Sine Hump" );
pattern       = int(   input( " Select a Data Pattern:         " ) );
minTemp       = float( input( " Minimum Temperature:           " ) );
maxTemp       = float( input( " Maximum Temperature:           " ) );
tempSAF       =        input( " Insert Stuck-At Error? (Y/N):  " );
if tempSAF == 'Y':
  SAFValue    = float( input( "  Stuck-At Error Value:         " ) );
  SAFStart    = int(   input( "  Stuck-At Error Start:         " ) );
  SAFEnd      = int(   input( "  Stuck-At Error End:           " ) );
noise         =        input( " Insert Noise? (Y/N):           " );
if noise == 'Y':
  noiseMax    = float( input( "  Maximum Noise Variation:      " ) );

# Performing Auxiliary Calculations/Operations/Safeguards
random.seed( );
filename = filename + ".txt";
dataFile = open( filename, 'w' );
avgTemp  = ( maxTemp + minTemp ) / 2;
tempDif  = maxTemp - minTemp;
noiseMax = math.fabs( noiseMax );
if SAFEnd > ( length ):
  SAFEnd = length;

print( "\nGenerating Temperature Data File...\n\n" );

# Data Calculations
x    = range( length );
data = [];
if pattern == 1:
  for i in x:
    data.append( linFall( tempDif, length, i, maxTemp ) );
    i += 1;
elif pattern == 2:
  for i in x:
    data.append( linRise( tempDif, length, i, minTemp ) );
    i += 1;
elif pattern == 3:
  for i in x:
    data.append( fall( tempDif, length, i, minTemp ) );
    i += 1;
elif pattern == 4:
  for i in x:
    data.append( rise( tempDif, length, i, minTemp ) );
    i += 1;
elif pattern == 5:
  for i in x:
    data.append( dip( tempDif, length, i, minTemp ) );
    i += 1;
elif pattern == 6:
  for i in x:
    data.append( hump( tempDif, length, i, minTemp ) );
    i += 1;
else:
  print( "Apologies, but that pattern does not exist." );

# Adding Noise
if noise == 'Y':
  for i in x:
    data[i] = data[i] + random.uniform( -noiseMax, noiseMax );
    i += 1;

# Adding Stuck-At Fault
if tempSAF == 'Y':
  for i in range( SAFStart, SAFEnd ):
    data[i] = SAFValue;
    i += 1;

# Print Calculations
for i in x:
  dataFile.write( str( (x[i] * v_max ) / float(length)) + ", " + str( data[i] ) + "\n" );
  print( (x[i] * v_max ) / float(length), ", ", data[i] );
  i += 1;

# Close File and Terminate
dataFile.close( );
print( "\n\n\n" );



# END TempDataGen.py - EWG SDG

