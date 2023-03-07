# Demonstration of Markdown

---

__Advertisement :)__

- __[ura](https://github.com/hyaku-dl/urasunday)__ - A no-nonsense, simple and easy to use downloader for [urasunday.com](https://urasunday.com)

I hope ypu like these projects

---

## **Headers**

# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading

## Horizontal Rules

___

---

***

## **Emphasis**

**This is bold text**

__This is also bold text__

*This is italic text*

_This is also italic text_

~~Strikethrough~~

## **Blockquotes**

**### Nested Blockquotes**

> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.

### **Indented Nested Blockquotes**

> You can also use indents
    >> Like this
>>> Or dedent again
        >>>> And indent two times

## **Lists**

### **Unordered**

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
    - Marker character change forces new list start:
        * Ac tristique libero volutpat at
        + Facilisis in pretium nisl aliquet
        - Nulla volutpat aliquam velit
+ Very easy!

### **Ordered**

#### **Sequential Numbering**

You can use sequential numbering like the following

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

#### **Recommended WAy of Numbering**

...Or, you can keep all the numbers as `1.`

1. Lorem ipsum dolor sit amet
1. Consectetur adipiscing elit
1. Integer molestie lorem at massa

#### **Offset Numbering**

57. This list starts from `57`
1. And I use the number `1`, yet still gets the number `58`


## **Code**

This is for the `inline code`

### **Indented code**

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

### **Block code fences**

```
Sample text here...
```

#### **Syntax Higlighting**

Specify the language after the first three backticks (` ``` `) with the language. In this example, or javascript, it is `js`.

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

### Custom Alignment

| Left | Center | Right |
| :--- | :----: | ----: |
| This is left-aligned | This is centered | This is right-aligned |

## Links

Follow my socials:

- [anilist](https://anilist.co/user/whinyaan)
- [email](whinyaan@protonmail.com)
- [github](https://github.com/whinee)
- [reddit](https://reddit.com/user/whi-nyaan)
- [twitter](https://twitter.com/whi_nyaan)

[hover over hereee](https://whinyaan.xyz "now, click")

## Images

![Alternative Text](https://whine.deta.dev/assets/images/icons/icon.png)

Like links, Images also have a footnote style syntax

![My Logo!][id]

With a reference later in the document defining the URL location:

[id]: https://whine.deta.dev/assets/images/icons/icon.png "My Very Pretty Logo!"
