{ system ? builtins.currentSystem }:

let
  pkgs = import <nixpkgs> { inherit system; };
in
pkgs.mkShell {
  name = "idx-env";

  buildInputs = with pkgs; [
    python311
    # Add other dependencies as needed, like:
    # git
    # any other command line tool
  ];

  packages = with pkgs; [
    (python311.withPackages (ps: with ps; [
      google-adk
    ]))
    # Add other python packages as needed
  ];

  shellHook = ''
    # Add this to make python find the right packages in nix store
    export PYTHONPATH=${pkgs.lib.makeBinPath packages}/lib/python3.11/site-packages:$PYTHONPATH
    export PATH=$PATH:${pkgs.lib.makeBinPath packages}/bin:./.pip_packages/bin
    echo "idx-env activated"
    direnv allow
  '';
}