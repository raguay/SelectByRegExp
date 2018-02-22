## SelectByRegExp

Plugin for [fman.io](https://fman.io) that allows you to select files in the current pane based on a regular expression.

To install this plugin, use [fman's built-in command](https://fman.io/docs/installing-plugins).

### Usage

When you press **Shift+r** (I'm using my Vim Keymappings), Fman will ask for a regular expression. Once you give one, it will select files in the current directory that matches the regular expression.

It also stores past regular expresstions so that you can quickly search for them also. You can use the `Select Reg Exp To Remove` command to remove an expression from the history.

### Features

 - Select/Deselect files based on regular expressions.
 - Keep a history of selections.