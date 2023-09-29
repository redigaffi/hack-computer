let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd /mnt/c/Users/jordi/Desktop/nand2tetris/projects/07
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +7 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm
badd +9 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/test.vm
badd +8 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/test.tst
badd +20 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunctionVME.tst
badd +540 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/op.py
badd +61 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/VMTranslator.py
badd +8 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.tst
badd +8 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.asm
badd +1 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.cmp
badd +0 /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.out
argglobal
%argdel
$argadd NvimTree_1
edit /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.cmp
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 30 + 87) / 174)
exe '2resize ' . ((&lines * 22 + 23) / 46)
exe 'vert 2resize ' . ((&columns * 143 + 87) / 174)
exe '3resize ' . ((&lines * 21 + 23) / 46)
exe 'vert 3resize ' . ((&columns * 143 + 87) / 174)
argglobal
enew
file NvimTree_1
balt /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd /mnt/c/Users/jordi/Desktop/nand2tetris/projects
wincmd w
argglobal
balt /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.asm
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd /mnt/c/Users/jordi/Desktop/nand2tetris/projects
wincmd w
argglobal
if bufexists(fnamemodify("/mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.out", ":p")) | buffer /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.out | else | edit /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.out | endif
if &buftype ==# 'terminal'
  silent file /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.out
endif
balt /mnt/c/Users/jordi/Desktop/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.cmp
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 2 - ((1 * winheight(0) + 10) / 21)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 0
lcd /mnt/c/Users/jordi/Desktop/nand2tetris/projects
wincmd w
3wincmd w
exe 'vert 1resize ' . ((&columns * 30 + 87) / 174)
exe '2resize ' . ((&lines * 22 + 23) / 46)
exe 'vert 2resize ' . ((&columns * 143 + 87) / 174)
exe '3resize ' . ((&lines * 21 + 23) / 46)
exe 'vert 3resize ' . ((&columns * 143 + 87) / 174)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
