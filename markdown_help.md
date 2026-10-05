---
title: Lorem ipsum dolor sit amet 
description: Nullam urna elit, malesuada eget finibus ut, ac tortor. 
icon: material/emoticon-happy
---
# Heading 1
## Heading 2
This is body text **bold** *italic* ***bold italic***

This is ~~strikethrough~~

This is ==highlighted==

This is <mark>highlighted<mark>

This <sub>is subscript</sub> and this <sup>is superscript</sup>

## Blockquotes

> blockquotes
>> nested blockquotes
> ### Can add headings
> - and bullets and other things

## Ordered lists
1. This
1. Is 
1. A 
1. List

## Unordered lists

- This
- Is an
- unordered list
    - we
    - can 
    - also 
    - indent
- back to main list

    some paragraph text

- and back again

[Subscribe to our newsletter](#){ .md-button }

# Code
You can insert `inline code` like this.

You can also create code blocks:

    <html>
      <head>
      </head>
    </html>
    
or like this:

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

And can use sytax highlighting:
```python
def myfunction(a,b)
    return a*b
```

# Links
Straight link:
[BBC](https://www.bbc.co.uk)

Link with title on hover:
[BBC](https://www.bbc.co.uk "British news site")

Link in new tab:
[BBC](https://www.bbc.co.uk){target=_blank}

Quickly embed url or email address:

<https://www.bbc.co.uk>

<me@email.com>

Inline links:
<a href="../../../assets/pins-short.png" target="_blank">analogue pins for the x and y axes</a>.



# Images
![This is an image](img/image.png){ align=left }

![This is an image](img/image.png){ align=right }

![This is an image](img/image.png){ align=center }

![This is an image](img/image.png){ width=300 }

![This is an image](img/image.png)
/// caption
Image caption
///

Image with link

[![This is an image](img/image.png)](https://bbc.co.uk)

# Embedding HTML
This <em>word</em> is italic.

# Tables
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

Alignment:

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

E.g.

| Break Beam Sensor     | micro:bit Connection              |
| :-------------------- | :-------------------------------- |
| Sensor (with 3 wires) | P13 3-pin connector               |
| LED (with 2 wires)    | Any GND and 3V3 pins, e.g. on P7 |


# Horizontal rule

---

# Icons and emojis
Emojis from [https://fontawesome.com/search](https://fontawesome.com/search), [https://pictogrammers.com/library/mdi/](https://pictogrammers.com/library/mdi/). [https://primer.style/octicons/](https://primer.style/octicons/)

:smile:
:fontawesome-solid-video:
:material-chat-alert-outline:
:material-bird:
:octicons-cpu-24:

!!! type "optional explicit title within double quotes"
    Any number of other indented markdown elements.

    This is the second paragraph.

# Heading ids

Add an id to a heading:

### My Custom Heading {#custom-id}

Link to the heading from somewhere else:

[Heading IDs](#custom-id)




# Checklists

- [x] Buy dog food
- [ ] Buy dog
- [ ] Name dog

# Custom variables
Use {{ bmlgithub }} to reference the main Github for Bitmakelab in a document.  Using this in a link will open a tab in Github:

[2D Parts]({{ bmlgithub }}/kit making/2D parts){target=_blank}

Use {{ bmlgithubpages }} to reference the Githubpages for Bitmakelab in a document.  Using this in a link will open a tab direct to the resource being linked to:

[Student Worksheet]({{ bmlgithubpages }}/introduction/Introduction 0.02 - Microbit Expansion/Introduction 0.02 - Microbit Expansion.pdf)

See mkdocs.yml for definitions of these and to add other ones.



























