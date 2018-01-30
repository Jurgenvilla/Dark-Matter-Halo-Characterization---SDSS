#Para checkar los datos si estan en los rangos esperados 

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Ell_U.eps'
p './Ell_Scale_length.dat' u 1
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Ell_G.eps'
p './Ell_Scale_length.dat' u 2
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Ell_R.eps'
p './Ell_Scale_length.dat' u 3
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Ell_I.eps'
p './Ell_Scale_length.dat' u 4
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Ell_Z.eps'
p './Ell_Scale_length.dat' u 5
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'S0_U.eps'
p './S0_Scale_length.dat' u 1
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'S0_G.eps'
p './S0_Scale_length.dat' u 2
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'S0_R.eps'
p './S0_Scale_length.dat' u 3
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'S0_I.eps'
p './S0_Scale_length.dat' u 4
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'S0_Z.eps'
p './S0_Scale_length.dat' u 5
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Sab_U.eps'
p './Sab_Scale_length.dat' u 1
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Sab_G.eps'
p './Sab_Scale_length.dat' u 2
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Sab_R.eps'
p './Sab_Scale_length.dat' u 3
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Sab_I.eps'
p './Sab_Scale_length.dat' u 4
reset
set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Sab_Z.eps'
p './Sab_Scale_length.dat' u 5
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Scd_U.eps'
p './Scd_Scale_length.dat' u 1
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Scd_G.eps'
p './Scd_Scale_length.dat' u 2
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Scd_R.eps'
p './Scd_Scale_length.dat' u 3
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Scd_I.eps'
p './Scd_Scale_length.dat' u 4
reset

set terminal postscript eps enhanced color font 'Helvetica,10'
set output 'Scd_Z.eps'
p './Scd_Scale_length.dat' u 5
reset