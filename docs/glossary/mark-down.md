## Headers

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Callouts

```markdown
!!! attention
    Any number of other indented markdown elements.

!!! caution
    Any number of other indented markdown elements.

!!! danger
    Any number of other indented markdown elements.

!!! error
    Any number of other indented markdown elements.

!!! hint
    Any number of other indented markdown elements.

!!! important
    Any number of other indented markdown elements.

!!! info
    Any number of other indented markdown elements.

!!! note
    Any number of other indented markdown elements.

!!! tip
    Any number of other indented markdown elements.
```

... becomes ...

> !!! attention
>     Any number of other indented markdown elements.
>
> !!! caution
>     Any number of other indented markdown elements.
>
> !!! danger
>     Any number of other indented markdown elements.
>
> !!! error
>     Any number of other indented markdown elements.
>
> !!! hint
>     Any number of other indented markdown elements.
>
> !!! important
>     Any number of other indented markdown elements.
>
> !!! info
>     Any number of other indented markdown elements.
>
> !!! note
>     Any number of other indented markdown elements.
>
> !!! tip
>     Any number of other indented markdown elements.

## Emphasis

```markdown
Emphasis, aka italics, with single *asterisks* or _underscores_.
Strong emphasis, aka bold, with double **asterisks** or __underscores__.
Combined emphasis with **asterisks and _underscores_**.
Strike-through uses two tildes. ~~Scratch this.~~
```

... becomes ...

> Emphasis, aka italics, with *asterisks* or _underscores_.
>
> Strong emphasis, aka bold, with **asterisks** or __underscores__.
>
> Combined emphasis with **asterisks and _underscores_**.
>
> Strike-through uses two tildes. ~~Scratch this.~~

## Lists

(In this example, leading and trailing spaces are shown with with dots: ⋅)

```markdown
1. First ordered list item
2. Another item
....* Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
....1. Ordered sub-list
4. And another item.

I am a paragraph

* Unordered list can use asterisks
- Or minuses
+ Or pluses
```

... becomes ...

> 1. First ordered list item
> 2. Another item
>     * Unordered sub-list.
> 1. Actual numbers don't matter, just that it's a number
>     1. Ordered sub-list
> 4. And another item.
>
> I am a paragraph
>
> * Unordered list can use asterisks
>
> - Or minuses
>
> + Or pluses

## Links

There are two ways to create links.

```markdown
[I'm an inline-style link](https://www.google.com)
[I'm an inline-style link with title](https://www.google.com "Google's Homepage")
[I'm a relative reference to a repository file](../blob/master/LICENSE)
[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
```

... becomes ...

> [I'm an inline-style link](https://www.google.com)
> [I'm an inline-style link with title](https://www.google.com "Google's Homepage")
> [I'm a relative reference to a repository file](../blob/master/LICENSE)
> [You can use numbers for reference-style link definitions][1]
>
> Or leave it empty and use the [link text itself].
>
> [1]: http://slashdot.org
> [link text itself]: http://www.reddit.com

## Images

```markdown
![alt text](../cdf/img/consumer.png "Descriptive Text"){{: style="height:48px;width:48px;align:center;"}
```

... becomes ...

> Here's our image (hover to see the title text):
> ![alt text](../cdf/img/consumer.png "Descriptive Text"){: style="height:48px;width:48px;align:center;"}
>

## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM and *Markdown Here* supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

```markdown
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
```

... becomes ...

> Colons can be used to align columns.
>
> | Tables        | Are           | Cool |
> | ------------- |:-------------:| -----:|
> | col 3 is      | right-aligned | $1600 |
> | col 2 is      | centered      |   $12 |
> | zebra stripes | are neat      |    $1 |
>
> There must be at least 3 dashes separating each header cell. The outer pipes ( \| ) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.
>
> Markdown | Less | Pretty
> --- | --- | ---
> *Still* | `renders` | **nicely**
> 1 | 2 | 3

## Blockquotes

```m
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.
```

becomes:

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.

## Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

```no-highlight
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

## Horizontal Rule

```markdown
Three or more...

---

Hyphens
```

... becomes ...

---

Hyphens

## Line Breaks

My basic recommendation for learning how line breaks work is to experiment and discover -- hit &lt;Enter&gt; once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.

Here are some things to try out:

```markdown
Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
```

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also begins a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
