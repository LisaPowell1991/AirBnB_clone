{ pkgs }: {
  deps = [
		pkgs.nodePackages.prettier
    pkgs.python39Packages.pycodestyle
    pkgs.vim
  
  ];
}