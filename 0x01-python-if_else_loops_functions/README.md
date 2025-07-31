# Complete Markdown Guide

Markdown is a lightweight markup language that allows you to format text using plain text syntax. It's widely used for documentation, README files, and web content.

## Headers

```markdown
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header
```

## Text Formatting

### Basic Formatting
- **Bold text**: `**bold**` or `__bold__`
- *Italic text*: `*italic*` or `_italic_`
- ***Bold and italic***: `***bold and italic***`
- ~~Strikethrough~~: `~~strikethrough~~`

### Code Formatting
- `Inline code`: Use backticks around text
- Code blocks: Use triple backticks

```python
# Code block example
def hello_world():
    print("Hello, World!")
```

## Lists

### Unordered Lists
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```

### Ordered Lists
```markdown
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested numbered item
3. Third item
```

## Links and Images

### Links
- Basic link: `[Link text](https://example.com)`
- Link with title: `[Link text](https://example.com "Title")`
- Reference link: `[Link text][reference]`

### Images
- Basic image: `![Alt text](image-url)`
- Image with title: `![Alt text](image-url "Title")`

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |
```

### Table Alignment
```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Text | Text   | Text  |
```

## Blockquotes

```markdown
> This is a blockquote
> 
> It can span multiple lines
> 
> > Nested blockquotes are also possible
```

## Horizontal Rules

Create horizontal lines using:
```markdown
---
***
___
```

## Line Breaks

- Two spaces at the end of a line creates a line break
- Empty line creates a paragraph break

## Escaping Characters

Use backslash `\` to escape special characters:
```markdown
\*This won't be italic\*
\# This won't be a header
```

## Advanced Features

### Task Lists (GitHub Flavored Markdown)
```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

### Footnotes
```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

### Definition Lists
```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### Abbreviations
```markdown
*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
```

## Code Syntax Highlighting

Specify language after opening triple backticks:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```

```bash
# Bash commands
ls -la
cd /path/to/directory
```

## Common Use Cases

### README Files
Perfect for project documentation, installation instructions, and usage examples.

### Documentation
Technical documentation, API references, and user guides.

### Note-Taking
Simple, portable format for notes that can be easily converted to other formats.

### Blog Posts
Many static site generators (Jekyll, Hugo) use Markdown for content.

## Best Practices

1. **Consistency**: Use consistent formatting throughout your document
2. **Readability**: Remember that Markdown should be readable as plain text
3. **Spacing**: Use blank lines to separate sections for better readability
4. **Headers**: Use proper header hierarchy (don't skip levels)
5. **Alt Text**: Always include descriptive alt text for images

## Tools and Editors

### Online Editors
- Dillinger.io
- StackEdit
- Typora (desktop)

### IDE Extensions
- VS Code: Markdown Preview Enhanced
- Atom: Markdown Preview Plus
- Sublime Text: MarkdownEditing

## Converting Markdown

Markdown can be converted to:
- HTML (most common)
- PDF
- Word documents
- LaTeX
- Presentations (reveal.js, etc.)

Popular conversion tools include Pandoc, which can convert between many formats.

---

*This guide covers the most commonly used Markdown features. Different platforms may support additional extensions or have slight variations in syntax.*