#!/usr/bin/env python
# -*- coding: utf-8 -*-


import misc


class FileType:
    def __init__(self, name, extension, *, prism_name=""):
        self.name = name
        self.extension = extension

        self.prism_name = prism_name


_prism_types = (
    FileType("ABAP"         , "abap"        , prism_name="abap"        ),
    FileType("ActionScript" , "as"          , prism_name="actionscript"),
    FileType("Ada"          , "ada"         , prism_name="ada"         ),
    FileType("APL"          , "apl"         , prism_name="apl"         ),
    FileType("AppleScript"  , "scpt"        , prism_name="applescript" ),
    FileType("AppleScript"  , "scptd"       , prism_name="applescript" ),
    FileType("AppleScript"  , "applescript" , prism_name="applescript" ),
    FileType("AutoIt"       , "au3"         , prism_name="autoit"      ),
    FileType("AutoHotkey"   , "ahk"         , prism_name="autohotkey"  ),
    FileType("Bash"         , "sh"          , prism_name="bash"        ),
    FileType("Bash"         , "bash"        , prism_name="bash"        ),
    FileType("BASIC"        , "bas"         , prism_name="basic"       ),
    FileType("Batch"        , "bat"         , prism_name="batch"       ),
    FileType("Batch"        , "cmd"         , prism_name="batch"       ),
    FileType("Bison"        , "y"           , prism_name="bison"       ),
    FileType("Brainfuck"    , "b"           , prism_name="brainfuck"   ),
    FileType("Brainfuck"    , "bf"          , prism_name="brainfuck"   ),
    FileType("Bro"          , "bro"         , prism_name="bro"         ),
    FileType("Bro"          , "br"          , prism_name="bro"         ),
    FileType("C"            , "c"           , prism_name="c"           ),
    FileType("C"            , "h"           , prism_name="c"           ),
    FileType("C#"           , "cs"          , prism_name="csharp"      ),
    FileType("C++"          , "cpp"         , prism_name="cpp"         ),
    FileType("C++"          , "hpp"         , prism_name="cpp"         ),
    FileType("CoffeeScript" , "coffee"      , prism_name="coffeescript"),
    FileType("CoffeeScript" , "litcoffee"   , prism_name="coffeescript"),
    FileType("Crystal"      , "rpt"         , prism_name="crystal"     ),
    FileType("CSS"          , "css"         , prism_name="css"         ),
    FileType("D"            , "d"           , prism_name="d"           ),
    FileType("Dart"         , "dart"        , prism_name="dart"        ),
    FileType("Diff"         , "diff"        , prism_name="diff"        ),
    FileType("Docker"       , "dockerfile"  , prism_name="docker"      ),
    FileType("Eiffel"       , "e"           , prism_name="eiffel"      ),
    FileType("Eiffel"       , "es"          , prism_name="eiffel"      ),
    FileType("Elixir"       , "ex"          , prism_name="elixir"      ),
    FileType("Elixir"       , "exs"         , prism_name="elixir"      ),
    FileType("Erlang"       , "erl "        , prism_name="erlang"      ),
    FileType("Erlang"       , "hrl"         , prism_name="erlang"      ),
    FileType("F#"           , "fs"          , prism_name="fsharp"      ),
    FileType("F#"           , "fsi"         , prism_name="fsharp"      ),
    FileType("F#"           , "fsx"         , prism_name="fsharp"      ),
    FileType("Fortran"      , "f"           , prism_name="fortran"     ),
    FileType("Fortran"      , "for"         , prism_name="fortran"     ),
    FileType("Fortran"      , "f90"         , prism_name="fortran"     ),
    FileType("Fortran"      , "f95"         , prism_name="fortran"     ),
    FileType("Fortran"      , "f03"         , prism_name="fortran"     ),
    FileType("Gherkin"      , "feature"     , prism_name="gherkin"     ),
    FileType("GLSL"         , "vert"        , prism_name="glsl"        ),
    FileType("GLSL"         , "frag"        , prism_name="glsl"        ),
    FileType("Go"           , "go"          , prism_name="go"          ),
    FileType("GraphQL"      , "graphql"     , prism_name="graphql"     ),
    FileType("Groovy"       , "groovy"      , prism_name="groovy"      ),
    FileType("Groovy"       , "gvy"         , prism_name="groovy"      ),
    FileType("Groovy"       , "gy"          , prism_name="groovy"      ),
    FileType("Groovy"       , "gsh"         , prism_name="groovy"      ),
    FileType("Haml"         , "haml"        , prism_name="haml"        ),
    FileType("Handlebars"   , "handlebars"  , prism_name="handlebars"  ),
    FileType("Handlebars"   , "hbs"         , prism_name="handlebars"  ),
    FileType("Haskell"      , "hs"          , prism_name="haskell"     ),
    FileType("Haskell"      , "lhs"         , prism_name="haskell"     ),
    FileType("Haxe"         , "hx"          , prism_name="haxe"        ),
    FileType("Haxe"         , "hxml"        , prism_name="haxe"        ),
    FileType("HTML"         , "html"        , prism_name="markup"      ),
    FileType("HTML"         , "htm"         , prism_name="markup"      ),
    FileType("Inform 7"     , "i6"          , prism_name="inform7"     ),
    FileType("Inform 7"     , "i7"          , prism_name="inform7"     ),
    FileType("Ini"          , "ini"         , prism_name="ini"         ),
    FileType("J"            , "j"           , prism_name="j"           ),
    FileType("Jade"         , "jade"        , prism_name="jade"        ),
    FileType("Java"         , "java"        , prism_name="java"        ),
    FileType("JavaScript"   , "js"          , prism_name="javascript"  ),
    FileType("Jolie"        , "ol"          , prism_name="jolie"       ),
    FileType("Jolie"        , "iol"         , prism_name="jolie"       ),
    FileType("JSON"         , "json"        , prism_name="json"        ),
    FileType("Julia"        , "jl"          , prism_name="julia"       ),
    FileType("Keyman"       , "kps"         , prism_name="keyman"      ),
    FileType("Kotlin"       , "kt"          , prism_name="kotlin"      ),
    FileType("Kotlin"       , "kts"         , prism_name="kotlin"      ),
    FileType("LaTeX"        , "latex"       , prism_name="latex"       ),
    FileType("Less"         , "less"        , prism_name="less"        ),
    FileType("LiveScript"   , "ls"          , prism_name="livescript"  ),
    FileType("LOLCODE"      , "lol"         , prism_name="lolcode"     ),
    FileType("LOLCODE"      , "lols"        , prism_name="lolcode"     ),
    FileType("Lua"          , "lua"         , prism_name="lua"         ),
    FileType("Makefile"     , "makefile"    , prism_name="makefile"    ),
    FileType("Markdown"     , "md"          , prism_name="markdown"    ),
    FileType("MATLAB"       , "m"           , prism_name="matlab"      ),
    FileType("MEL"          , "mel"         , prism_name="mel"         ),
    FileType("Mizar"        , "miz"         , prism_name="mizar"       ),
    FileType("Monkey"       , "monkey"      , prism_name="monkey"      ),
    FileType("NASM"         , "asm"         , prism_name="nasm"        ),
    FileType("Nim"          , "nim"         , prism_name="nim"         ),
    FileType("NSIS"         , "nsi"         , prism_name="nsis"        ),
    FileType("NSIS"         , "nsh"         , prism_name="nsis"        ),
    FileType("Objective-C"  , "m"           , prism_name="objectivec"  ),
    FileType("OCaml"        , "ml"          , prism_name="ocaml"       ),
    FileType("OCaml"        , "mli"         , prism_name="ocaml"       ),
    FileType("Oz"           , "oz"          , prism_name="oz"          ),
    FileType("Pascal "      , "pas"         , prism_name="pascal"      ),
    FileType("Perl"         , "pl"          , prism_name="perl"        ),
    FileType("PHP"          , "php"         , prism_name="php"         ),
    FileType("PowerShell"   , "ps1"         , prism_name="powershell"  ),
    FileType("Processing"   , "pde"         , prism_name="processing"  ),
    FileType("Prolog"       , "pro"         , prism_name="prolog"      ),
    FileType("Prolog"       , "P"           , prism_name="prolog"      ),
    FileType(".properties"  , "properties"  , prism_name="properties"  ),
    FileType("Pure"         , "pure"        , prism_name="pure"        ),
    FileType("Python"       , "py"          , prism_name="python"      ),
    FileType("Python"       , "pyw"         , prism_name="python"      ),
    FileType("Q"            , "q"           , prism_name="q"           ),
    FileType("Qore"         , "q"           , prism_name="qore"        ),
    FileType("Qore"         , "qm"          , prism_name="qore"        ),
    FileType("Qore"         , "qtest"       , prism_name="qore"        ),
    FileType("R"            , "r"           , prism_name="r"           ),
    FileType("React JSX"    , "jsx"         , prism_name="jsx"         ),
    FileType("Reason"       , "re"          , prism_name="reason"      ),
    FileType("Rip"          , "rip"         , prism_name="rip"         ),
    FileType("Ruby"         , "rb"          , prism_name="ruby"        ),
    FileType("Ruby"         , "rbw"         , prism_name="ruby"        ),
    FileType("Rust"         , "rs"          , prism_name="rust"        ),
    FileType("Rust"         , "rlib"        , prism_name="rust"        ),
    FileType("Rust"         , "rafto"       , prism_name="rust"        ),
    FileType("SAS"          , "sas"         , prism_name="sas"         ),
    FileType("Sass (Sass)"  , "sass"        , prism_name="sass"        ),
    FileType("Sass (Scss)"  , "scss"        , prism_name="scss"        ),
    FileType("Scala"        , "scala"       , prism_name="scala"       ),
    FileType("Scala"        , "sc"          , prism_name="scala"       ),
    FileType("Scheme"       , "scm"         , prism_name="scheme"      ),
    FileType("Scheme"       , "ss"          , prism_name="scheme"      ),
    FileType("SQL"          , "sql"         , prism_name="sql"         ),
    FileType("Stylus"       , "styl"        , prism_name="stylus"      ),
    FileType("Swift"        , "swift"       , prism_name="swift"       ),
    FileType("Tcl"          , "tcl"         , prism_name="tcl"         ),
    FileType("Textile"      , "textile"     , prism_name="textile"     ),
    FileType("TypeScript"   , "ts"          , prism_name="typescript"  ),
    FileType("Verilog"      , "v"           , prism_name="verilog"     ),
    FileType("VHDL"         , "vhdl"        , prism_name="vhdl"        ),
    FileType("YAML"         , "yaml"        , prism_name="yaml"        ),
    FileType("YAML"         , "yml"         , prism_name="yaml"        ),
    FileType("XML"          , "xml"         , prism_name="markup"      ),
    FileType("DotSettings"  , "dotsettings" , prism_name="markup"      ),
    FileType("resx"         , "resx"        , prism_name="markup"      ),
    FileType("VS project"   , "csproj"      , prism_name="markup"      ),
    FileType(".config"      , "config"      , prism_name="markup"      ),
    FileType(".vsixmanifest", "vsixmanifest", prism_name="markup"      ),
)


def get(filename, istext):
    if not istext:
        return FileType("Binary", "")
    filename = misc.getlastpathpart(filename).lower()
    for filetype in _prism_types:
        ext = filetype.extension
        if filename == ext or filename.endswith("." + ext):
            return filetype
    return FileType("Plain text", "", prism_name="none")
