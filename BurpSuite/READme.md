### Intruder

Intruder helps us to automate requests, which is very userful when fuzzing or bruteforcing.

### Positions tab
When we are looking to perform an attack with Intruder, the first thing we need to do is look at _positions._ Positions tell Intruder where to insert payloads (which we will look at in upcoming tasks).

The payloads will be generated in positions where `§` exists

On the right-hand side of the interface, we have the buttons labelled "Add §", "Clear §", and "Auto §":

-   **Add** lets us define new positions by highlighting them in the editor and clicking the button.
-   **Clear** removes all defined positions, leaving us with a blank canvas to define our own.
-   **Auto** attempts to select the most likely positions automatically; this is useful if we cleared the default positions and want them back.

### Attack Types

There are four attack types available:
-   Sniper
-   Battering ram
-   Pitchfork
-   Cluster bomb

#### Sniper 

- Is the most common.
- When conducting a sniper attack, we provide _one_ set of payloads.
- In a sniper attack, Intruder will take each position and substitute each payload into it in turn.

Notice how Intruder starts with the first position (`username`) and tries each of our payloads, then moves to the second position and tries the same payloads again. We can calculate the number of requests that Intruder Sniper will make as

- `requests = numberOfWords * numberOfPositions`

This quality makes Sniper very good for single-position attacks (e.g. a password bruteforce if we know the username or _fuzzing for API endpoints).

#### Battering Ram

Like Sniper, Battering ram takes _one_ set of payloads (e.g. one wordlist). _Un_like Sniper, the Battering ram puts the same payload in _every_ position rather than in each position in turn.

Intruder will take each payload and substitute it into every position _at once._

![image](https://user-images.githubusercontent.com/99975622/234567622-34407aea-f067-4935-a69f-8cda32661e54.png)


#### Pitchfork

Pitchfork is the attack type you are most likely to use. It may help to think of Pitchfork as being like having numerous Snipers running simultaneously. Where Sniper uses _one_ payload set (which it uses on every position simultaneously), Pitchfork uses one payload set per position (up to a maximum of 20) and iterates through them all at once.

This type of attack can take a little time to get your head around.

![image](https://user-images.githubusercontent.com/99975622/234569200-24aa9712-410b-400d-985d-6927cd49d367.png)


See how Pitchfork takes the first item from each list and puts them into the request, one per position? It then repeats this for the next request: taking the second item from each list and substituting it into the template. Intruder will keep doing this until one (or all) of the lists run out. Ideally, our payload sets should be identical lengths when working in Pitchfork, as Intruder will stop testing as soon as one of the lists is complete. For example, if we have two lists, one with 100 lines and one with 90 lines, Intruder will only make 90 requests, and the final ten items in the first list will not get tested.

#### Cluster Bomb

Cluster bomb allows us to choose multiple payload sets: one per position, up to a maximum of 20; however, whilst Pitchfork iterates through each payload set simultaneously, Cluster bomb iterates through each payload set individually, making sure that every possible combination of payloads is tested.

![image](https://user-images.githubusercontent.com/99975622/234569764-0917aeba-51a2-4faa-9557-58d0499cdcc5.png)


Cluster Bomb will iterate through every combination of the provided payload sets to ensure that every possibility has been tested. This attack-type can create a _huge_ amount of traffic (_equal to the number of lines in each payload set multiplied together_), so be careful!

### Payloads

The **Payload Sets** section allows us to choose which position we want to configure a set for as well as what type of payload we would like to use.

-   When we use an attack type that only allows for a single payload set (i.e. Sniper or Battering Ram), the dropdown menu for "Payload Set" will only have one option, regardless of how many positions we have defined.
-   If we are using one of the attack types that use multiple payload sets (i.e. Pitchfork or Cluster Bomb), then there will be one item in the dropdown for each position.  
    _**Note:** Multiple positions should be read from top to bottom, then left to right when being assigned numbers in the "Payload set" dropdown. For example, with two positions (_`username=§pentester§&password=§Expl01ted§`_), the first item in the payload set dropdown would refer to the username field, and the second would refer to the password field.  

The second dropdown in this section allows us to select a "payload type". By default, this is a "Simple list" -- which, as the name suggests, lets us load in a wordlist to use. There are many other payload types available -- some common ones include: `Recursive Grep`, `Numbers`, and `Username generator`.

-   **Payload Options** differ depending on the payload type we select for the current payload set. For example, a "Simple List" payload type will give us a box to add and remove payloads to and from the set:  
    ![Screenshot of the payload options for a simple list](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/aa7a5c278455b7f3066410b941354448.png)  
    We can do this manually using the "Add" text box, paste lines in with "Paste", or "Load..." from a file. The "Remove" button removes the currently selected line _only_. The "Clear" button clears the entire list. Be warned: loading extremely large lists in here can cause Burp to crash!  
    By contrast, the options for a `Numbers` payload type allows us to change options such as the range of numbers used and the base that we are working with.   
    
-   **Payload Processing** allows us to define rules to be applied to each payload in the set before being sent to the target. For example, we could capitalise every word or skip the payload if it matches a regex. You may not use this section particularly regularly, but you will definitely appreciate it when you _do_ need it!  

-   Finally, we have the **Payload Encoding** section. This section allows us to override the default URL encoding options that are applied automatically to allow for the safe transmission of our payload. Sometimes it can be beneficial to _not_ URL encode these standard "unsafe" characters, which is where this section comes in. We can either adjust the list of characters to be encoded or outright uncheck the "URL-encode these characters" checkbox.

### Extender

The default view in the Extender interface gives us an overview of the extensions that we have loaded into Burp Suite. There are none in the screenshot above -- we will change this in the next few tasks. The first box (towards the top of the interface) provides us with a list of extensions that we have installed and allows us to activate or deactivate them for this project.

The options to the left of this box allow us to uninstall extensions with the Remove button or install new ones from files on our disk with the Add button. These could be either modules that we have coded or modules that have been made available on the internet but are not in the BApp store. The Up and Down buttons in this section control the order that installed extensions are listed in. Extensions are invoked in _descending_ order based on this list. In other words: all traffic passing through Burp Suite will be passed through each extension in order, starting at the top of the list and working down. This can be very important when dealing with extensions that modify the requests as some may counteract or otherwise hinder one another.  

Towards the bottom of the window, we have Details, Output and Errors for the currently selected module. These can be used to view module information, as well as for debugging.

The Burp App Store (or BApp Store for short) gives us a way to easily list official extensions and integrate them seamlessly with Burp Suite. Extensions can be written in a variety of languages -- most commonly Java (which integrates into the framework automatically) or Python (which requires the Jython interpreter -- more on this in the next task!).  
  
Let's start by installing a Java extension, just to get a feel for the BApp store.  
  
The [Request Timer](https://github.com/portswigger/request-timer) extension (Written by Nick Taylor) allows us to log the time that each request we send takes to receive a response; this can be extremely useful for discovering the presence of (and exploiting) time-based vulnerabilities. For example, if a login form takes an extra second to process requests that contain a valid username than it does for accounts that do not exist, then we can quickly generate a list of possible usernames and use the difference in times to see which usernames are valid.

Switch over to the "BApp Store" sub-tab, then search for "Request Timer". There should only be one result. Click on the returned Extension, then click "Install":![Installation steps for installing the Request Timer from the BApp store](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/7a9077f19a68a81647874639a6afaeb4.gif)

Notice that a new tab appeared in the main menu at the top of the screen. Different extensions have different behaviours: some merely add a new item to right-click context menus; others create entirely new tabs in the main menu bar.

As this was just an example of using the BApp store, we won't cover using the Request Timer here; however, switching to the new tab and taking a look is highly recommended!

The Burp Suite Decoder module allows us to manipulate data. As the name suggests, we can _decode_ information that we capture during an attack, but we can also _encode_ data of our own, ready to be sent to the target. Decoder also allows us to create _hashsums_ of data, as well as providing a Smart Decode feature which attempts to decode provided data recursively until it is back to being plaintext (like the "Magic" function of [Cyberchef](https://gchq.github.io/CyberChef/)).  

Let's select the Decoder tab from the top menu and take a look at the options available:  
![Initial view when accessing decoder](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/3ad809fdb51d36584e0cfc809d9f18e4.png)

This interface offers us a number of options.

1.  The box on the left is where we would paste or type text to be encoded or decoded. As with most other modules of Burp Suite, we can also send data here from other sections of the framework by right-clicking and choosing _Send to Decoder._  
    
2.  We have the option to select between treating the input as text or hexadecimal byte values at the top of the list on the right.
3.  Further down the list, we have dropdown menus to _Encode_, _Decode_ or _Hash_ the input.
4.  Finally, we have the "Smart Decode" feature, which attempts to decode the input automatically.

![The four sections noted in the above list labelled as described](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/986cbf61cc820eb26720f1d9ed4b5a64.png)

As we add data into the input field, the interface will duplicate itself to contain the output of our transformation. We can then choose to operate on this using the same options:  
![Demonstrating how the interface duplicates itself when data is entered, allowing for further transformations to be applied.](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/257ef62054a79fe68172310bfcb4c002.png)

We will look at the available transformations in the upcoming tasks!

_**Decoding/Encoding Methods:**_  

Let's take a closer look at the manual encoding and decoding options. These are the same whether we choose the decoding or encoding menu:  
![Screenshot showing the manual encoding options listed below](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/8ce7c550edf3a79cafbb7be8468793ff.png)

-   **Plain:** Plaintext is what we have before performing any transformations.
-   **URL:** URL encoding is used to make data safe to transfer in the URL of a web request. It involves exchanging characters for their ASCII character code in hexadecimal format, preceded by a percentage symbol (`%`). Url encoding is an extremely useful method to know for any kind of web application testing.  
    For example, let's encode the forward-slash character (`/`). The [ASCII character code](https://www.asciitable.com/) for a forward slash is 47. This is "2F" in hexadecimal, making the URL encoded forward-slash `%2F`. We can confirm this with Decoder by typing a forward slash in the input box, then selecting `Encode as` -> `URL`:  
    ![Confirming that / translates to %2F using Burp Suite Decoder](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/72ecaaf06fc248457d61c079d6d98e8f.png)  
    
-   **HTML:** Encoding text as HTML Entities involves replacing special characters with an ampersand (`&`) followed by either a hexadecimal number or a reference to the character being escaped, then a semicolon (`;`). For example, a quotation mark has its own reference: `&quot;`. When this is inserted into a webpage, it will be replaced by a double quotation mark (`"`). This encoding method allows special characters in the HTML language to be rendered safely in HTML pages and has the added bonus of being used to prevent attacks such as [XSS](https://owasp.org/www-community/attacks/xss/) (Cross-Site Scripting).  
    When we use the HTML option in Decoder, we can encode any character as its HTML escaped format or decode captured HTML entities. For example, to decode the quotation mark we looked at before, we type in the encoded variant then choose `Decode as` -> `HTML`:  
    ![Demonstration of decoding the HTML encoded quotation mark used previously as an example](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/99ccb4aba6cb243b7c3b990e82061a86.png)  
    
-   **Base64:** Another widely used encoding method, base64 is used to encode any data in an ASCII-compatible format. It was designed to take binary data (e.g. images, media, programs) and encode it in a format that would be suitable to transfer over virtually any medium. How this works under the hood is not important at this point; however, if you are interested, you can read the maths behind it [here](https://stackabuse.com/encoding-and-decoding-base64-strings-in-python).
-   **ASCII Hex:** This option converts data between ASCII representation and hexadecimal representation. For example, the word "ASCII" can be converted into the hexadecimal number "4153434949". Each letter in the original data is taken individually and converted from numeric ASCII representation into hexadecimal. For example, the letter "A" in ASCII has a decimal [character code](https://www.asciitable.com/) of 65. In hexadecimal, this is 41. Similarly, the letter "S" can be converted to hexadecimal 53, and so on.
-   **Hex**, **Octal**, and **Binary:** These encoding methods all apply only to numeric inputs. They convert between decimal, hexadecimal, octal (base eight) and binary.
-   **Gzip:** Gzip provides a way to _compress_ data. It is widely used to reduce the size of files and pages before they are sent to your browser. Smaller pages mean faster loading times, which is highly desirable for developers looking to increase their SEO score and avoid annoying their customers. Decoder allows us to manually encode and decode gzip data, although this can be hard to process as it is often not valid ASCII/Unicode. For example:  
    ![Demonstration that Gzip compressed data isn't usually readable as ASCII](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/01db98e37c59a26e307eb29cd9e04139.png)

We can layer any of these on top of each other. For example, we could take a phrase ("Burp Suite Decoder"), convert it to ASCII Hex, and then into octal:  
![Demonstrating layering encoding methods on top of each other](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/9066bc864745b22c4b151133ee5bca4c.gif)  

When combined, these methods give us a great deal of control over the data that we are encoding or decoding.

As you may have noticed from the examples, each encoding/decoding method is colour coded to allow us to quickly and easily see what transformation has been applied.  

---

_**Hex Format:**_  

Inputting data in ASCII format is great, but sometimes we need to be able to edit our input byte-by-byte. For this, we can use "Hex View" by choosing "Hex" above the decoding options:  
![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/704444afc761deabd6a8a3492dffd89b.png)  

This setting allows us to view and edit our text in hexadecimal byte format -- a very useful trick if we are working with binary files or other non-ASCII data.  

---

_**Smart Decode:**_  

Finally, let's take a look at the "Smart Decode" option. This feature of Decoder attempts to automatically decode encoded text. For example, `&#x42;&#x75;&#x72;&#x70;&#x20;&#x53;&#x75;&#x69;&#x74;&#x65;`, is automatically recognised as being HTML encoded and is automatically decoded accordingly:  
![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/e6330851dfa9ea47e3d2d54ab78b0023.gif)

This feature is far from perfect, but it can be very useful for quickly decoding chunks of unknown data


### Comparer
_Comparer_ allows us to compare two pieces of data, either by ASCII words or by bytes.

### Sequencer
Sequencer is one of those tools that rarely ever gets used in CTFs and other lab environments but is an essential part of a real-world web app penetration test.

In short, Sequencer allows us to measure the _entropy_ (or randomness, in other words) of "tokens" -- strings that are used to identify something and should, in theory, be generated in a cryptographically secure manner. For example, we may wish to analyse the randomness of a session cookie or a **C**ross-**S**ite **R**equest **F**orgery (CSRF) token protecting a form submission. If it turns out that these tokens are not generated securely, then we can (in theory) predict the values of upcoming tokens. Just imagine the implications of this if the token in question is used for password resets...

There are two main methods we can use to perform token analysis with Sequencer:

-   **Live capture** is the more common of the two methods -- this is the default sub-tab for Sequencer. Live capture allows us to pass a request to Sequencer, which we know will create a token for us to analyse. For example, we may wish to pass a POST request to a login endpoint into Sequencer, as we know that the server will respond by giving us a cookie. With the request passed in, we can tell Sequencer to start a live capture: it will then make the same request thousands of times automatically, storing the generated token samples for analysis. Once we have accumulated enough samples, we stop Sequencer and allow it to analyse the captured tokens.
-   **Manual load** allows us to load a list of pre-generated token samples straight into Sequencer for analysis. Using Manual Load means we don't have to make thousands of requests to our target (which is both loud and resource intensive), but it does mean that we need to obtain a large list of pre-generated tokens!

We will start by capturing a request to `http://MACHINE_IP/admin/login/` in the Proxy. Right-click on the request and choose "Send to Sequencer":  
![GIF showing the request capture and sending to Sequencer](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/a48b3787771b855bb76d1618960de6ec.gif)

Notice in the "Token Location Within Response" section we have the option to select between Cookie, Form field, and Custom location. In this instance, we are testing the `loginToken`, so select the radio button for "Form field":  
![Screenshot showing changing the token location to test the login token](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/9bb4ea43eb0acb59dee493699d336930.png)  

We can safely leave all other options at default in this instance, so let's go ahead and click the "Start live capture" button!  

A new window will now pop up telling us that we are performing a live capture and showing us how many tokens we have so far captured. We need to wait until we have a reasonable number of tokens captured (around 10,000 should do); the more tokens we have, the more accurate our analysis.  

Once you have around 10,000 tokens captured, click "Pause", then select the "Analyze now" button:  
![Screenshot showing the live capture controls with the pause and analyse now buttons highlighted](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/715caf9a950bdd3a3c9ec4a5360ae9ca.png)  

_**Note:** We could also have chosen to "Stop" the capture; however, by choosing to pause it instead, we leave the option resume the capture open, should the report not have enough samples to calculate the entropy of the token accurately._  

If we wanted to receive periodic updates on the analysis, we could also have checked the "Auto analyze" checkbox. Doing this would tell Burp to perform the entropy analysis every 2000 requests or so, giving us frequent updates that will get progressively more accurate as more samples are loaded into Sequencer.

It is worth noting that at this point, we could also choose to copy or save the captured tokens for further analysis later on.  

Having clicked the "Analyze now" button, Burp will proceed to analyse the entropy of our token and generate a report. We will look through this in the next task.


#### Analysis

Now that we have a report for the entropy analysis of our token, it's time to analyse it!

Burp performs dozens of tests on the token samples that it captured. We won't be looking at all of these as it would take far more than a single task to do so (and it would get very maths-intensive to break each technique apart). Instead, we will focus on the generated summary; however, you are encouraged to look through all of the test results for yourself.

The generated entropy analysis report is split into four primary sections -- the first of these being a summary of the results:  
![Screenshot of the summary view in the analysis report](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d9e176315f8850e719252ed/room-content/f4dcdfcbb03e65edd6b31974f09d2254.png)

The summary gives us an overall result; the effective entropy; an analysis of the reliability of the results; and a summary of the sample taken.

Collectively, these will often be enough to determine whether the token is generated safely or not; however, in some instances, we may need to have a look at the test results directly -- this can be done in the "Character-level analysis" and "Bit-level analysis" tabs. As mentioned previously, we will not be going into these to avoid delving into the depths of statistical-analysis mathematics in a beginner-friendly room. In short, with an estimated 1% chance of being incorrect based on the data provided (Significance level: 1%), Burp has calculated that the effective entropy of our token _should_ be around 117 bits. This is an excellent level of entropy to have in a secure token, although it should be noted that it is impossible to say with absolute assurance that this calculation is entirely accurate, simply due to the nature of the topic.
