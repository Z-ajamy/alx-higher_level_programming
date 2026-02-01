# 0x14 JavaScript - Web Scraping

## Overview

This project introduces web scraping techniques in JavaScript using Node.js. You will learn how to make HTTP requests, parse JSON data, manipulate files, and extract information from websites and APIs. Web scraping is a powerful technique for automating data collection and integration with external services. This project covers both API consumption and HTML parsing.

## Learning Objectives

By the end of this project, you should be able to:

- Make HTTP requests using the `request` module
- Work with JSON data parsing and serialization
- Handle file operations (reading and writing)
- Parse HTML and extract data using CSS selectors
- Work with asynchronous operations and callbacks
- Implement error handling in network operations
- Use the command line to pass arguments to scripts
- Consume RESTful APIs
- Process and transform scraped data
- Save data to files

## Requirements

### General Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 18.04 LTS using Node.js (version 10.x)
- All files should end with a newline
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/node`
- Code should follow good practices without using `var`
- All functions should be documented
- No need to push a `package.json`, but one can be used to manage dependencies

### Required Modules

```bash
# Install dependencies
npm install request
npm install cheerio
npm install fs
```

## Project Structure

A typical 0x14-javascript_web_scraping project includes:

```
0x14-javascript_web_scraping/
├── 0-readme.js
├── 1-number.js
├── 2-read_file.js
├── 3-starwars_title.js
├── 4-starwars_count.js
├── 5-request_store.js
├── 6-completed_tasks.js
├── README.md
└── package.json (optional)
```

## Core Concepts

### 1. HTTP Requests

Making requests to web servers to fetch data.

```javascript
const request = require('request');

request('https://api.example.com/data', (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }
    console.log(body);
});
```

### 2. JSON Handling

Parsing JSON data from APIs and converting objects to JSON.

```javascript
const data = '{"name":"John","age":30}';
const obj = JSON.parse(data);      // String to Object
const json = JSON.stringify(obj);  // Object to String

console.log(obj.name);  // 'John'
```

### 3. File Operations

Reading and writing files in Node.js.

```javascript
const fs = require('fs');

// Read file
fs.readFile('file.txt', 'utf8', (error, data) => {
    if (error) throw error;
    console.log(data);
});

// Write file
fs.writeFile('file.txt', 'content', (error) => {
    if (error) throw error;
    console.log('File written');
});
```

### 4. HTML Parsing

Extracting data from HTML using CSS selectors.

```javascript
const cheerio = require('cheerio');

const html = '<div class="item"><h2>Title</h2></div>';
const $ = cheerio.load(html);

console.log($('.item h2').text());  // 'Title'
```

### 5. Asynchronous Programming

Handling operations that don't complete immediately.

```javascript
// Callback pattern
function fetchData(callback) {
    setTimeout(() => {
        callback(null, 'data');
    }, 1000);
}

fetchData((error, data) => {
    if (error) console.log(error);
    else console.log(data);
});
```

## Detailed Task Examples

### Task 0: Readme (0-readme.js)
Read a file and display its contents.

**Concepts:** File reading, error handling

```javascript
#!/usr/bin/node
/**
 * Read and display the contents of a file
 * Usage: ./0-readme.js <filepath>
 */
const fs = require('fs');

const filepath = process.argv[2];

if (!filepath) {
    console.log('Usage: ./0-readme.js <filepath>');
    process.exit(1);
}

fs.readFile(filepath, 'utf8', (error, data) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(data);
});
```

**Usage:**
```bash
./0-readme.js myfile.txt
```

### Task 1: Number (1-number.js)
Write the number of command-line arguments to a file.

**Concepts:** File writing, command-line arguments

```javascript
#!/usr/bin/node
/**
 * Write the count of command-line arguments to a file
 * Usage: ./1-number.js <filepath>
 */
const fs = require('fs');

const filepath = process.argv[2];

if (!filepath) {
    console.log('Usage: ./1-number.js <filepath>');
    process.exit(1);
}

// Number of arguments minus the first 2 (node path and script path)
const count = process.argv.length - 2;

fs.writeFile(filepath, count.toString(), (error) => {
    if (error) {
        console.error(error);
        return;
    }
});
```

**Usage:**
```bash
./1-number.js myfile.txt arg1 arg2 arg3
```

### Task 2: Read File (2-read_file.js)
Read a file and print its number of lines.

**Concepts:** File reading, string splitting, line counting

```javascript
#!/usr/bin/node
/**
 * Read a file and display the number of lines
 * Usage: ./2-read_file.js <filepath>
 */
const fs = require('fs');

const filepath = process.argv[2];

if (!filepath) {
    console.log('Usage: ./2-read_file.js <filepath>');
    process.exit(1);
}

fs.readFile(filepath, 'utf8', (error, data) => {
    if (error) {
        console.error(error);
        return;
    }
    
    // Split by newlines and filter empty lines
    const lines = data.split('\n').filter(line => line.length > 0);
    console.log(lines.length);
});
```

**Usage:**
```bash
./2-read_file.js myfile.txt
```

### Task 3: Star Wars Title (3-starwars_title.js)
Fetch Star Wars movie title from the API using movie ID.

**Concepts:** HTTP requests, JSON parsing, API consumption

```javascript
#!/usr/bin/node
/**
 * Fetch and display a Star Wars movie title
 * Usage: ./3-starwars_title.js <movie_id>
 */
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
    console.log('Usage: ./3-starwars_title.js <movie_id>');
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    
    if (response.statusCode !== 200) {
        console.error('Error:', response.statusCode);
        return;
    }
    
    try {
        const movie = JSON.parse(body);
        console.log(movie.title);
    } catch (err) {
        console.error('Error parsing JSON:', err);
    }
});
```

**Usage:**
```bash
./3-starwars_title.js 1
# Output: A New Hope
```

### Task 4: Star Wars Character Count (4-starwars_count.js)
Count how many times a character appears in Star Wars movies.

**Concepts:** HTTP requests, filtering, looping through results

```javascript
#!/usr/bin/node
/**
 * Count Star Wars movie appearances of a character
 * Usage: ./4-starwars_count.js <character_id>
 */
const request = require('request');

const characterId = process.argv[2];

if (!characterId) {
    console.log('Usage: ./4-starwars_count.js <character_id>');
    process.exit(1);
}

const url = 'https://swapi.dev/api/films/';

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    
    try {
        const data = JSON.parse(body);
        let count = 0;
        
        // Iterate through all films
        for (const film of data.results) {
            // Check if character appears in this film
            for (const character of film.characters) {
                if (character.includes(`/people/${characterId}/`)) {
                    count++;
                }
            }
        }
        
        console.log(count);
    } catch (err) {
        console.error('Error:', err);
    }
});
```

**Usage:**
```bash
./4-starwars_count.js 4
# Output: Number of appearances for character ID 4
```

### Task 5: Store Request Data (5-request_store.js)
Fetch data from a URL and save it to a file.

**Concepts:** HTTP requests, file writing, error handling

```javascript
#!/usr/bin/node
/**
 * Fetch webpage and save to file
 * Usage: ./5-request_store.js <url> <filepath>
 */
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

if (!url || !filepath) {
    console.log('Usage: ./5-request_store.js <url> <filepath>');
    process.exit(1);
}

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    
    fs.writeFile(filepath, body, 'utf8', (err) => {
        if (err) {
            console.error(err);
            return;
        }
    });
});
```

**Usage:**
```bash
./5-request_store.js 'https://api.example.com/data' output.txt
```

### Task 6: Completed Tasks (6-completed_tasks.js)
Compute how many tasks are completed by user ID from an API.

**Concepts:** JSON parsing, array operations, filtering

```javascript
#!/usr/bin/node
/**
 * Display count of completed tasks per user
 * Usage: ./6-completed_tasks.js <api_url>
 */
const request = require('request');

const url = process.argv[2];

if (!url) {
    console.log('Usage: ./6-completed_tasks.js <api_url>');
    process.exit(1);
}

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    
    try {
        const tasks = JSON.parse(body);
        const completedByUser = {};
        
        // Count completed tasks per user
        for (const task of tasks) {
            if (task.completed) {
                if (!completedByUser[task.userId]) {
                    completedByUser[task.userId] = 0;
                }
                completedByUser[task.userId]++;
            }
        }
        
        console.log(completedByUser);
    } catch (err) {
        console.error('Error:', err);
    }
});
```

**Usage:**
```bash
./6-completed_tasks.js 'https://jsonplaceholder.typicode.com/todos'
```

## Advanced Web Scraping Examples

### HTML Parsing with Cheerio

```javascript
const request = require('request');
const cheerio = require('cheerio');

request('https://example.com', (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    
    const $ = cheerio.load(body);
    
    // Extract titles
    $('h1').each((index, element) => {
        console.log($(element).text());
    });
    
    // Extract links
    $('a').each((index, element) => {
        console.log($(element).attr('href'));
    });
});
```

### Parsing CSV-like Data

```javascript
const fs = require('fs');

fs.readFile('data.csv', 'utf8', (error, data) => {
    if (error) throw error;
    
    const lines = data.split('\n');
    const headers = lines[0].split(',');
    
    const records = lines.slice(1).map(line => {
        const values = line.split(',');
        const obj = {};
        headers.forEach((header, index) => {
            obj[header.trim()] = values[index].trim();
        });
        return obj;
    });
    
    console.log(records);
});
```

### Chaining Requests

```javascript
const request = require('request');

function fetchUserData(userId, callback) {
    request(`https://api.example.com/users/${userId}`, (error, response, body) => {
        if (error) {
            callback(error, null);
            return;
        }
        
        const user = JSON.parse(body);
        
        // Fetch related data
        request(`https://api.example.com/users/${userId}/posts`, (err, res, postBody) => {
            if (err) {
                callback(err, null);
                return;
            }
            
            user.posts = JSON.parse(postBody);
            callback(null, user);
        });
    });
}

fetchUserData(1, (error, user) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(user);
});
```

## HTTP Status Codes

Common status codes when web scraping:

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Data retrieved successfully |
| 301 | Moved Permanently | Follow redirect |
| 400 | Bad Request | Check request format |
| 401 | Unauthorized | Need authentication |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limited, wait before retrying |
| 500 | Server Error | Server issue, try again later |

## Error Handling Patterns

### Basic Try-Catch

```javascript
try {
    const data = JSON.parse(body);
    console.log(data);
} catch (error) {
    console.error('Parse error:', error.message);
}
```

### Request Error Handling

```javascript
request(url, (error, response, body) => {
    if (error) {
        console.error('Request error:', error);
        return;
    }
    
    if (response.statusCode !== 200) {
        console.error('HTTP error:', response.statusCode);
        return;
    }
    
    try {
        const data = JSON.parse(body);
        // Process data
    } catch (parseError) {
        console.error('Parse error:', parseError);
    }
});
```

### File Operation Error Handling

```javascript
fs.readFile(filepath, 'utf8', (error, data) => {
    if (error) {
        if (error.code === 'ENOENT') {
            console.error('File not found');
        } else if (error.code === 'EACCES') {
            console.error('Permission denied');
        } else {
            console.error('Read error:', error);
        }
        return;
    }
    // Process data
});
```

## Best Practices

1. **Validate Input Arguments**
   ```javascript
   const url = process.argv[2];
   if (!url) {
       console.log('Usage: ./script.js <url>');
       process.exit(1);
   }
   ```

2. **Handle Errors Gracefully**
   ```javascript
   request(url, (error, response, body) => {
       if (error) {
           console.error(error);
           return;
       }
   });
   ```

3. **Parse JSON Safely**
   ```javascript
   try {
       const data = JSON.parse(body);
   } catch (error) {
       console.error('Invalid JSON:', error);
   }
   ```

4. **Check HTTP Status Codes**
   ```javascript
   if (response.statusCode !== 200) {
       console.error('HTTP Error:', response.statusCode);
       return;
   }
   ```

5. **Use Meaningful Variable Names**
   ```javascript
   // Good
   const movieTitle = movie.title;
   const completedTasks = tasks.filter(t => t.completed);
   
   // Avoid
   const t = movie.title;
   const ct = tasks.filter(t => t.completed);
   ```

6. **Close Resources Properly**
   ```javascript
   fs.readFile(file, 'utf8', (error, data) => {
       if (error) {
           console.error(error);
           return;  // Resources cleaned up automatically
       }
   });
   ```

7. **Respect Rate Limits**
   ```javascript
   // Add delays between requests if scraping multiple pages
   const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
   
   async function scrapeWithDelay(urls) {
       for (const url of urls) {
           // Fetch and process
           await delay(1000);  // Wait 1 second between requests
       }
   }
   ```

## Common Issues

### Issue: "Cannot find module 'request'"
```bash
# Solution: Install the module
npm install request
```

### Issue: "401 Unauthorized" Error
- Check if API requires authentication
- Use API keys or tokens if provided
- Some APIs require headers

```javascript
const options = {
    url: 'https://api.example.com/data',
    headers: {
        'Authorization': 'Bearer YOUR_TOKEN'
    }
};

request(options, (error, response, body) => {
    // Handle response
});
```

### Issue: "ENOTFOUND" Error
- Check URL is correct
- Verify internet connection
- Check for typos in domain name

### Issue: Timeout on Large Files
- Increase timeout
- Stream data instead of loading all at once

```javascript
const options = {
    url: url,
    timeout: 10000  // 10 second timeout
};

request(options, callback);
```

## Package.json Example

```json
{
    "name": "web-scraping",
    "version": "1.0.0",
    "description": "JavaScript web scraping project",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "dependencies": {
        "request": "^2.88.0",
        "cheerio": "^1.0.0-rc.3"
    },
    "author": "ALX Student",
    "license": "ISC"
}
```

## Useful APIs for Testing

- **Star Wars API**: `https://swapi.dev/api/`
- **JSONPlaceholder**: `https://jsonplaceholder.typicode.com/`
- **OpenWeatherMap**: `https://api.openweathermap.org/`
- **GitHub API**: `https://api.github.com/`
- **REST Countries**: `https://restcountries.com/v3.1/`

## Testing Your Scripts

```bash
# Test file reading
./0-readme.js README.md

# Test file writing
./1-number.js test.txt arg1 arg2 arg3

# Test API calls
./3-starwars_title.js 1

# Test data filtering
./6-completed_tasks.js 'https://jsonplaceholder.typicode.com/todos'
```

## Resources

- [Node.js fs Module](https://nodejs.org/api/fs.html)
- [Request Module Documentation](https://github.com/request/request)
- [Cheerio Documentation](https://cheerio.js.org/)
- [JSON.parse/stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [RESTful API Design](https://restfulapi.net/)
- [Web Scraping Ethics](https://en.wikipedia.org/wiki/Web_scraping#Legal_and_ethical_issues)

## Key Takeaways

- **File Operations**: Use `fs.readFile()` and `fs.writeFile()` for file I/O
- **HTTP Requests**: Use `request` module to fetch data from URLs
- **JSON Handling**: Use `JSON.parse()` to convert strings to objects
- **Error Handling**: Always check for errors in callbacks
- **Status Codes**: Verify HTTP responses are successful (200)
- **HTML Parsing**: Use Cheerio for CSS selector-based HTML parsing
- **Command Line Args**: Access via `process.argv` array
- **Asynchronous**: Web operations are non-blocking with callbacks

## License

This project is part of the ALX Software Engineering Program.
