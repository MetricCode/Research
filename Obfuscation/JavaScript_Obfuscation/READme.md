# Javascript Deobfuscation
## @Author : M3tr1c_r00t
![image](https://user-images.githubusercontent.com/99975622/222302781-6f0e8c12-2d2d-4572-95ae-f036d9edf2bd.png)

-js can be internal or external.
### What is obfuscation
Obfuscation is a technique used to make a script more difficult to read by humans but allows it to function the same from a technical point of view, though performance may be slower.

Java script usually resides on the client side and hence is visible to the user while other languages such as python and php reside on the server side.

js is very open to the users in plain text and that's why it is usually obfuscated.

### Reasons for obfuscation
- Hiding the original and the functioning of a javascript code to prevent it being reused and copied.
- To provide a security layer when dealing with authentication or encryption to prevent attacks on vulnerabilities that may be found within the code. 
- For malicious scripts to prevent detection by intrusion detection and prevention systems.

### Obfuscation
#### Code minification
this is having the entire code in a single long line.

For this, we can use ```https://javascript-minifier.com/```

minified code is usually saved as ```.min.js```

#### Code Packing 
It is usally noted by the initial function ```function(p,a,c,k,e,d)```

A packer obfuscation tool usually attempts to convert all words and symbols of the code into a list or a dictionary and then refer to them using the (p,a,c,k,e,d) function to re-build the original code during execution. The (p,a,c,k,e,d) can be different from one packer to another. However, it usually contains a certain order in which the words and symbols of the original code were packed to know how to order them during execution.

We can use this for obfuscation:
```http://beautifytools.com/javascript-obfuscator.php```

#### Further Obfuscation
We can use some tools to further obfuscate our code.
For example:
- ```https://obfuscator.io/``` 
Before you click on obfuscate, we need to change the string array encoding to base64 or any other.
- ```http://www.jsfuck.com/```

## Deobfuscation
### Minified Deobfuscation
We can beautify our code through our browser by the developer tools.

- In js , we can open the browser debugger with [ CTRL+SHIFT+Z ] then click on the script you want to deobfuscate. We can click on the curl brackets on the lower left of the tab and beautify the code.
- ```https://prettier.io/playground/``` and ```https://beautifier.io/``` are good online tools to deobfuscate the code.

## Unpacking Deobfuscation
```http://www.jsnice.org/``` is a good tool( We should click on the options button next to the "Nicify JavaScript" button, and de-select "Infer types" to reduce cluttering the code with comments.

Ensure you do not leave any empty lines before the script, as it may affect the deobfuscation process and give inaccurate results.)

### Decoding Obfuscated code
- base64
- hex 
- ROT13
To encode hex; 
```echo "test"| xxd -p```
To decode hex;
```echo "test"|xxd -p -r ```
To encode and decode ROT13
```echo "test"| tr 'A-Za-z' 'N-ZA-Mn-za-m'```


## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
