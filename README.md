## Trailing Punctuation

This is a Sublime Text 3 plugin which will add or toggle punctuation at the end of a line.

### Installation

Use Package Control, search for "Trailing Punctuation".

### Usage

This adds two keyboard shortcuts: <kbd>Alt+,</kbd> and <kbd>Alt+;</kbd>. Respectively, these will add a comma and a semicolon at the end of the current line (or lines, in the case of multiple selections or a multiple-line selection).

If the line already ends with the character, it is removed (toggled).

If the line ends with the other character, it is replaced (comma becomes semicolon, semicolon becomes comma).

For example, assume the cursor is on this line and you press <kbd>Alt+,</kbd>. Each line shows the behaviour of pressing the shortcut key again.

```js
var foo = 1;
var foo = 1,
var foo = 1
var foo = 1,
```

First, the semicolon is replaced with a comma. The second time, it removes the comma. The third time, it inserts a trailing comma.

In all cases, the current cursor position and selection is unchanged.

It is even smart enough to ignore comments and whitespace at the end of lines. (`·` represents whitespace below)

```
var·whyDoPeople····
var·notUseSemicolons·//·???···

// select all, press `Alt+;`

var·whyDoPeople;····
var·notUseSemicolons;·//·???···
```

On lines which are empty, or only contain whitespace or comments, no characters are inserted.
