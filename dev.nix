{ pkgs ? import <nixpkgs> { system = builtins.currentSystem; } }:

pkgs.mkShell {
  buildInputs = [pkgs.direnv];
}