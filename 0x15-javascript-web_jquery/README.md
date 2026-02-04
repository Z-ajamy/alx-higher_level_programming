# 0x15 JavaScript - Web jQuery

## Overview

This project introduces jQuery, a fast and concise JavaScript library that simplifies HTML document traversal, event handling, animation, and Ajax interactions. jQuery makes it easier to write client-side JavaScript code and provides cross-browser compatibility. You will learn how to manipulate the DOM, handle user events, make asynchronous requests, and create interactive web experiences.

## Learning Objectives

By the end of this project, you should be able to:

- Understand what jQuery is and why it's useful
- Select DOM elements using jQuery selectors
- Manipulate DOM elements (add, remove, modify content)
- Handle user events with jQuery
- Make Ajax requests to fetch data
- Work with HTML forms and input validation
- Animate elements on the page
- Chain jQuery methods
- Understand jQuery vs vanilla JavaScript
- Build interactive web applications with jQuery

## Requirements

### General Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted in the browser
- jQuery version 3.x is recommended
- HTML files must have a proper structure
- Use of `var` is not recommended; use best practices
- All scripts should be at the end of the body tag
- Comments should explain the purpose of code
- No page reload should occur for events

### Including jQuery

```html
<!-- From CDN -->
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

<!-- Or locally -->
<script src="jquery-3.2.1.min.js"></script>
```

## Project Structure

A typical 0x15-javascript-web_jquery project includes:

```
0x15-javascript-web_jquery/
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
├── 8-script.js
├── 9-script.js
├── 100-script.js
├── 101-script.js
├── 102-script.js
├── 103-script.js
└── README.md
```

## jQuery Fundamentals

### 1. jQuery Selectors

jQuery uses CSS selectors to find DOM elements.

```javascript
// Element selector
$('p')                    // All paragraphs
$('div')                  // All divs

// ID selector
$('#myId')               // Element with id="myId"

// Class selector
$('.myClass')            // All elements with class="myClass"

// Attribute selector
$('input[type="text"]')  // All text inputs

// Combination
$('div.container')       // Divs with class container
$('ul > li')            // Direct li children of ul

// Multiple selectors
$('h1, h2, h3')         // All h1, h2, h3 elements
```

### 2. DOM Manipulation

Changing content and structure of elements.

```javascript
// Get/Set content
$('#myDiv').text()              // Get text content
$('#myDiv').text('New text')    // Set text content
$('#myDiv').html()              // Get HTML content
$('#myDiv').html('<p>HTML</p>') // Set HTML content

// Add elements
$('#myDiv').append('<p>New</p>')      // Add to end
$('#myDiv').prepend('<p>New</p>')     // Add to beginning
$('<p>New</p>').appendTo('#myDiv')    // Alternative syntax

// Remove elements
$('#myDiv').remove()            // Remove element
$('#myDiv').empty()             // Remove children

// Modify attributes
$('#myImg').attr('src', 'image.png')      // Set attribute
$('#myDiv').attr('class', 'myClass')      // Set class
$('#myInput').val()                        // Get input value
$('#myInput').val('new value')             // Set input value

// Add/Remove classes
$('#myDiv').addClass('highlight')         // Add class
$('#myDiv').removeClass('highlight')      // Remove class
$('#myDiv').toggleClass('highlight')      // Toggle class
$('#myDiv').hasClass('highlight')         // Check class
```

### 3. Event Handling

Responding to user interactions.

```javascript
// Click event
$('#myButton').click(function() {
    console.log('Button clicked!');
});

// Multiple event types
$('#myElement').on('click', function() {
    // Handle click
});

$('#myElement').on('mouseover', function() {
    // Handle mouse over
});

// Multiple events at once
$('#myElement').on('click mouseover', function() {
    // Handle both events
});

// Event delegation (for dynamic elements)
$(document).on('click', '.dynamic-button', function() {
    // Handle clicks on dynamic buttons
});

// Other common events
$('#myInput').on('change', function() {
    // Input value changed
});

$('#myForm').on('submit', function(event) {
    event.preventDefault();  // Prevent form submission
    // Handle submit
});

$('input').on('focus', function() {
    // Input focused
});

$('input').on('blur', function() {
    // Input lost focus
});

// Remove event handlers
$('#myButton').off('click');
```

### 4. Effects and Animation

Animating elements on the page.

```javascript
// Show/Hide
$('#myDiv').show()          // Show element
$('#myDiv').hide()          // Hide element
$('#myDiv').toggle()        // Toggle visibility

// Fade effects
$('#myDiv').fadeIn()        // Fade in
$('#myDiv').fadeOut()       // Fade out
$('#myDiv').fadeToggle()    // Toggle fade
$('#myDiv').fadeTo(1000, 0.5)  // Fade to 50% opacity

// Slide effects
$('#myDiv').slideDown()     // Slide down
$('#myDiv').slideUp()       // Slide up
$('#myDiv').slideToggle()   // Toggle slide

// Custom animation
$('#myDiv').animate({
    left: '250px',
    opacity: 0.5
}, 1000);  // 1 second duration

// Stop animation
$('#myDiv').stop()
```

### 5. Ajax Requests

Fetching data without page reload.

```javascript
// Simple GET request
$.get('data.txt', function(data) {
    console.log(data);
});

// GET with parameters
$.get('api.php', { id: 123 }, function(data) {
    console.log(data);
});

// POST request
$.post('submit.php', { name: 'John' }, function(data) {
    console.log(data);
});

// More flexible ajax method
$.ajax({
    url: 'api.php',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        console.log(data);
    },
    error: function(error) {
        console.log('Error:', error);
    }
});

// Load HTML into element
$('#myDiv').load('page.html');

// With callback after load
$('#myDiv').load('page.html', function() {
    console.log('Content loaded');
});
```

## Detailed Task Examples

### Task 0: Update Div (0-script.js)
Update a div element when page loads.

**Concepts:** DOM selection, content manipulation, ready event

```javascript
/**
 * Update div#best_id text to "New content"
 */
$(document).ready(function() {
    $('#best_id').text('New content');
});
```

**HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="best_id">Old content</div>
    <script src="0-script.js"></script>
</body>
</html>
```

### Task 1: Add Header (1-script.js)
Add a header element to the page.

**Concepts:** Creating elements, appending to body

```javascript
/**
 * Add <header> element to the page
 */
$(document).ready(function() {
    $('body').prepend('<header>Best School</header>');
});
```

### Task 2: Toggle Class (2-script.js)
Toggle a class on an element when button is clicked.

**Concepts:** Event handling, class toggling, click events

```javascript
/**
 * Toggle class "red" on div#toggle_me when #toggle_switch is clicked
 */
$(document).ready(function() {
    $('#toggle_switch').click(function() {
        $('#toggle_me').toggleClass('red');
    });
});
```

**HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .red {
            color: red;
        }
    </style>
</head>
<body>
    <button id="toggle_switch">Toggle</button>
    <div id="toggle_me">Text to toggle</div>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="2-script.js"></script>
</body>
</html>
```

### Task 3: Add/Remove Classes (3-script.js)
Add a class to an element based on conditions.

**Concepts:** Multiple class operations, if statements

```javascript
/**
 * Add class "green" to div.item when not already green
 * Remove class "red" when not already red
 */
$(document).ready(function() {
    $('#add_class').click(function() {
        $('div.item').each(function() {
            if (!$(this).hasClass('green')) {
                $(this).addClass('green');
            }
            if ($(this).hasClass('red')) {
                $(this).removeClass('red');
            }
        });
    });
});
```

### Task 4: Toggle and Delete (4-script.js)
Toggle classes and remove elements.

**Concepts:** Multiple operations, element removal

```javascript
/**
 * Toggle class "black" on div#target
 * Delete element div.item on double click
 */
$(document).ready(function() {
    $('#toggle_it').click(function() {
        $('#target').toggleClass('black');
    });
    
    $('div.item').dblclick(function() {
        $(this).remove();
    });
});
```

### Task 5: Filter and List (5-script.js)
Create dynamic list items from data.

**Concepts:** Creating elements, loops, event delegation

```javascript
/**
 * Build a list of movies dynamically
 * Format: <li><h2>Movie Name</h2></li>
 */
$(document).ready(function() {
    const movies = ['Toy Story', 'The Lion King', 'Frozen'];
    
    movies.forEach(function(movie) {
        $('ul#list_movies').append(`<li><h2>${movie}</h2></li>`);
    });
});
```

**HTML:**
```html
<!DOCTYPE html>
<html>
<body>
    <ul id="list_movies"></ul>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="5-script.js"></script>
</body>
</html>
```

### Task 6: Fetch and Display Data (6-script.js)
Fetch data from API and display it.

**Concepts:** Ajax requests, data parsing, HTML insertion

```javascript
/**
 * Fetch data from OpenWeather API and display temp in #fahrenheit
 */
$(document).ready(function() {
    const apiUrl = 'https://api.openweathermap.org/data/2.5/weather?q=San Francisco&units=imperial&appid=YOUR_API_KEY';
    
    $.get(apiUrl, function(data) {
        $('#fahrenheit').text(data.main.temp);
    });
});
```

**HTML:**
```html
<!DOCTYPE html>
<html>
<body>
    <div id="fahrenheit"></div>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="6-script.js"></script>
</body>
</html>
```

### Task 7: Interactive Search (7-script.js)
Search and filter list items.

**Concepts:** Input events, filtering, conditional display

```javascript
/**
 * Filter list items based on search input
 */
$(document).ready(function() {
    $('#search_input').on('keyup', function() {
        const searchTerm = $(this).val().toLowerCase();
        
        $('ul#list_movies li').each(function() {
            const movieName = $(this).text().toLowerCase();
            if (movieName.includes(searchTerm)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});
```

### Task 8: Post Data (8-script.js)
Send form data via Ajax without page reload.

**Concepts:** Form submission, POST requests, event prevention

```javascript
/**
 * Submit form data via AJAX
 * POST to submit.php without page reload
 */
$(document).ready(function() {
    $('#form_id').submit(function(event) {
        event.preventDefault();
        
        const name = $('#form_id input[name="name"]').val();
        const value = $('#form_id input[name="value"]').val();
        
        $.post('submit.php', 
            { name: name, value: value },
            function(data) {
                $('body').prepend(data);
            }
        );
    });
});
```

### Task 9: Animated Updates (9-script.js)
Animate element changes.

**Concepts:** Animation, callbacks, chaining

```javascript
/**
 * Animate color change on header when button clicked
 */
$(document).ready(function() {
    $('#btn_id').click(function() {
        $('header').animate({
            color: 'red'
        }, 1000);
    });
});
```

### Task 100: Load/Update Multiple (100-script.js)
Load data from multiple sources.

**Concepts:** Multiple Ajax calls, data manipulation

```javascript
/**
 * Load translation based on dropdown selection
 */
$(document).ready(function() {
    $('#language_code').change(function() {
        const langCode = $(this).val();
        const url = `https://www.fourtonfish.com/hellospeaker/api.php?language=${langCode}`;
        
        $.get(url, function(data) {
            $('body h1').text(data.hello);
        });
    });
});
```

### Task 101: Complex Filtering (101-script.js)
Advanced filtering with multiple conditions.

**Concepts:** Complex selectors, multiple conditions

```javascript
/**
 * Filter movies by character count
 */
$(document).ready(function() {
    $('#search').on('keyup', function() {
        const searchTerm = $(this).val();
        
        $('div.item').filter(function() {
            const text = $(this).text();
            return text.indexOf(searchTerm) > -1;
        }).show().end().not(':has(:contains(' + searchTerm + '))').hide();
    });
});
```

### Task 102: Rich Animations (102-script.js)
Chain multiple animations.

**Concepts:** Animation chaining, delays

```javascript
/**
 * Animate element with multiple effects
 */
$(document).ready(function() {
    $('#start_animation').click(function() {
        const element = $('#animation_box');
        
        element
            .animate({ left: '100px' }, 1000)
            .animate({ top: '100px' }, 1000)
            .animate({ left: '0px' }, 1000)
            .animate({ top: '0px' }, 1000);
    });
});
```

### Task 103: Clear Form (103-script.js)
Reset and clear form inputs.

**Concepts:** Form handling, input clearing, event handling

```javascript
/**
 * Clear form inputs and reset to default
 */
$(document).ready(function() {
    $('#clear_form').click(function() {
        $('#my_form')[0].reset();
        // Or manually clear each field
        $('#name').val('');
        $('#email').val('');
        $('#message').val('');
    });
});
```

## jQuery vs Vanilla JavaScript

| Task | jQuery | Vanilla JS |
|------|--------|-----------|
| Select by ID | `$('#myId')` | `document.getElementById('myId')` |
| Select by class | `$('.myClass')` | `document.querySelectorAll('.myClass')` |
| Add class | `$el.addClass('cls')` | `el.classList.add('cls')` |
| Set text | `$el.text('txt')` | `el.textContent = 'txt'` |
| Set HTML | `$el.html('<p>x</p>')` | `el.innerHTML = '<p>x</p>'` |
| Show element | `$el.show()` | `el.style.display = 'block'` |
| Hide element | `$el.hide()` | `el.style.display = 'none'` |
| Click event | `$el.click(fn)` | `el.addEventListener('click', fn)` |
| Get value | `$el.val()` | `el.value` |
| AJAX GET | `$.get(url, fn)` | `fetch(url).then(r => r.text())` |

## Common jQuery Patterns

### Pattern 1: Document Ready
```javascript
$(document).ready(function() {
    // Code here runs when DOM is loaded
});

// Shorthand
$(function() {
    // Same as above
});
```

### Pattern 2: Method Chaining
```javascript
$('#myDiv')
    .addClass('highlight')
    .text('Updated')
    .fadeIn()
    .animate({ left: '100px' }, 1000);
```

### Pattern 3: Event Delegation
```javascript
// For existing and future elements
$(document).on('click', '.button', function() {
    console.log('Button clicked!');
});
```

### Pattern 4: Conditional Class Toggle
```javascript
if ($('#myDiv').hasClass('active')) {
    $('#myDiv').removeClass('active');
} else {
    $('#myDiv').addClass('active');
}

// Or simpler
$('#myDiv').toggleClass('active');
```

### Pattern 5: Each Loop
```javascript
$('li').each(function(index) {
    console.log(index + ': ' + $(this).text());
});
```

## Best Practices

1. **Always use $(document).ready()**
   ```javascript
   $(document).ready(function() {
       // Code here
   });
   ```

2. **Cache jQuery objects**
   ```javascript
   // Good - cache the selection
   const $button = $('#myButton');
   $button.click(function() {
       $button.fadeOut();
   });
   
   // Avoid - selects multiple times
   $('#myButton').click(function() {
       $('#myButton').fadeOut();
   });
   ```

3. **Use event delegation for dynamic content**
   ```javascript
   // Good - works for elements added later
   $(document).on('click', '.dynamic-btn', handler);
   
   // Avoid - only works for existing elements
   $('.dynamic-btn').click(handler);
   ```

4. **Prevent default behavior when needed**
   ```javascript
   $('#form').submit(function(event) {
       event.preventDefault();
       // Handle with AJAX instead
   });
   ```

5. **Minimize DOM manipulation**
   ```javascript
   // Good - single DOM manipulation
   let html = '';
   data.forEach(item => {
       html += `<li>${item}</li>`;
   });
   $('ul').html(html);
   
   // Avoid - multiple DOM operations
   data.forEach(item => {
       $('ul').append(`<li>${item}</li>`);
   });
   ```

6. **Use specific selectors**
   ```javascript
   // Good - specific selector
   $('#form input[type="text"]')
   
   // Avoid - too general
   $('input')
   ```

7. **Handle errors in AJAX**
   ```javascript
   $.ajax({
       url: 'api.php',
       success: function(data) {
           console.log('Success:', data);
       },
       error: function(error) {
           console.log('Error:', error);
       }
   });
   ```

## Useful jQuery Methods

```javascript
// DOM Traversal
$('div').parent()          // Parent element
$('div').children()        // Direct children
$('div').find('span')      // Descendants
$('div').siblings()        // Siblings
$('div').next()            // Next sibling
$('div').prev()            // Previous sibling

// DOM Manipulation
$('div').append(html)      // Add to end
$('div').prepend(html)     // Add to beginning
$('div').after(html)       // Add after element
$('div').before(html)      // Add before element
$('div').replaceWith(html) // Replace element
$('div').wrap('<section></section>')  // Wrap with element

// Utilities
$.each(array, function(i, item) {})  // Loop through array
$.inArray(value, array)              // Index of value
$.merge(arr1, arr2)                  // Merge arrays
$.extend(obj1, obj2)                 // Extend object
```

## Common Gotchas

### Gotcha 1: `this` vs `$(this)`
```javascript
// Wrong - 'this' is DOM element
$('button').click(function() {
    this.hide();  // Error - DOM elements don't have hide()
});

// Correct - wrap in jQuery
$('button').click(function() {
    $(this).hide();  // Works - jQuery method
});
```

### Gotcha 2: Forgetting to use $(this) in each()
```javascript
// Wrong
$('li').each(function() {
    text = $(this).text();  // Missing jQuery wrapper
});

// Correct
$('li').each(function() {
    $(this).text('new');
});
```

### Gotcha 3: Event handler not working on dynamic content
```javascript
// Wrong - only works for existing elements
$('.new-button').click(handler);

// Correct - works for future elements too
$(document).on('click', '.new-button', handler);
```

### Gotcha 4: Animation queue
```javascript
// Each call is queued
$('div').fadeOut();
$('div').fadeOut();  // Fades out twice!

// Use stop to clear queue
$('div').stop().fadeOut();
```

## Troubleshooting

### jQuery not loading
- Check script tag is before your code
- Verify jQuery URL is correct
- Check browser console for errors

```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="my-script.js"></script>
```

### Elements not found
- Verify selectors are correct
- Check element IDs/classes match
- Use browser dev tools to inspect

```javascript
console.log($('#myId').length);  // Should be 1 if found
```

### Events not firing
- Ensure code is in $(document).ready()
- Check selectors are correct
- Use event delegation for dynamic elements

## Resources

- [jQuery Official Documentation](https://api.jquery.com/)
- [jQuery Learning Center](https://learn.jquery.com/)
- [jQuery Selectors Reference](https://www.w3schools.com/jquery/jquery_selectors.asp)
- [jQuery Methods Reference](https://www.w3schools.com/jquery/jquery_ref_methods.asp)
- [jQuery AJAX Reference](https://api.jquery.com/#ajax)
- [Can I Use - jQuery](https://caniuse.com/jquery)

## Modern Alternatives

While jQuery is still widely used, modern JavaScript has caught up:

- **Vanilla JavaScript** - Modern JS (ES6+) is powerful and built-in
- **React** - Component-based framework
- **Vue.js** - Progressive framework
- **Angular** - Full-featured framework

For new projects, consider using modern frameworks, but jQuery remains valuable for:
- Quick scripts and prototypes
- Legacy project maintenance
- Learning DOM manipulation
- Simplifying cross-browser compatibility

## Key Takeaways

- **Selectors** - CSS-like syntax to find elements
- **DOM Manipulation** - Change content and structure
- **Events** - Respond to user interactions
- **Effects** - Animate changes smoothly
- **AJAX** - Load data without page reload
- **Chaining** - Combine multiple operations
- **Method Chaining** - More readable and efficient code
- **Ready Event** - Ensure DOM is loaded before running code

## License

This project is part of the ALX Software Engineering Program.
