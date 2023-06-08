aspects of penetration tests might significantly differ from a real attack, like:

- **Penetration tests are LOUD:** Usually, pentesters won't put much effort into trying to go undetected. Unlike real attackers, they don't mind being easy to detect, as they have been contracted to find as many vulnerabilities as they can in as many hosts as possible.
- **Non-technical attack vectors might be overlooked:** Attacks based on social engineering or physical intrusions are usually not included in what is tested.
- **Relaxation of security mechanisms:** While doing a regular penetration test, some security mechanisms might be temporarily disabled or relaxed for the pentesting team in favor of efficiency. Although this might sound counterintuitive, it is essential to remember that pentesters have limited time to check the network. Therefore, it is usually desired not to waste their time searching for exotic ways to bypass IDS/IPS, WAF, intrusion deception or other security measures, but rather focus on reviewing critical technological infrastructure for vulnerabilities.

On the other hand, real attackers won't follow an ethical code and are mostly unrestricted in their actions. Nowadays, the most prominent threat actors are known as **Advanced Persistent Threats (APT)**, which are highly skilled groups of attackers, usually sponsored by nations or organised criminal groups. They primarily target critical infrastructure, financial organisations, and government institutions. They are called persistent because the operations of these groups can remain undetected on compromised networks for long periods.

#### Red Team Engagements

To keep up with the emerging threats, red team engagements were designed to shift the focus from regular penetration tests into a process that allows us to clearly see our defensive team's capabilities at **detecting** and **responding** to a real threat actor.

They focus on detection and response rather than prevention.

Translated into the world of cybersecurity, red team engagements consist of emulating a real threat actor's **Tactics, Techniques and Procedures (TTPs)** so that we can measure how well our blue team responds to them and ultimately improve any security controls in place.

Every red team engagement will start by defining clear goals, often referenced as **crown jewels** or **flags**, ranging from compromising a given critical host to stealing some sensitive information from the target.

Usually, the blue team won't be informed of such exercises to avoid introducing any biases in their analysis. The red team will do everything they can to achieve the goals while remaining undetected and evading any existing security mechanisms like firewalls, antivirus, EDR, IPS and others. Notice how on a red team engagement, not all of the hosts on a network will be checked for vulnerabilities. A real attacker would only need to find a single path to its goal and is not interested in performing noisy scans that the blue team could detect.

It is important to note that the final objective of such exercises should never be for the red team to "beat" the blue team, but rather simulate enough TTPs for the blue team to learn to react to a real ongoing threat adequately

Red team engagements also improve on regular penetration tests by considering several attack surfaces:

- **Technical Infrastructure:** Like in a regular penetration test, a red team will try to uncover technical vulnerabilities, with a much higher emphasis on stealth and evasion.
- **Social Engineering:** Targeting people through phishing campaigns, phone calls or social media to trick them into revealing information that should be private.
- **Physical Intrusion:** Using techniques like lockpicking, RFID cloning, exploiting weaknesses in electronic access control devices to access restricted areas of facilities.

Depending on the resources available, the red team exercise can be run in several ways:

- **Full Engagement:** Simulate an attacker's full workflow, from initial compromise until final goals have been achieved.
- **Assumed Breach:** Start by assuming the attacker has already gained control over some assets, and try to achieve the goals from there. As an example, the red team could receive access to some user's credentials or even a workstation in the internal network.
- **Table-top Exercise:**  An over the table simulation where scenarios are discussed between the red and blue teams to evaluate how they would theoretically respond to certain threats. Ideal for situations where doing live simulations might be complicated.

### Teams and Functions Of an Engagement

There are several factors and people involved within a red team engagement. Everyone will have their mindset and methodology to approach the engagement personnel; however, each engagement can be broken into three teams or cells.

![image](https://github.com/MetricCode/Research/assets/99975622/dbf1e3ba-14aa-4826-ab12-e80cf175c0f8)

More ...

![image](https://github.com/MetricCode/Research/assets/99975622/961ea7e6-11b9-407d-9a18-d1b6362b8094)


#### Engagement Structure

A core function of the red team is adversary emulation.  it is commonly used to assess what a real adversary would do in an environment using their tools and methodologies. The red team can use various cyber kill chains to summarize and assess the steps and procedures of an engagement.

The blue team commonly uses cyber kill chains to map behaviors and break down an adversaries movement. The red team can adapt this idea to map adversary TTPs (**T**actics, **T**echniques, and **P**rocedures) to components of an engagement.

Below is a small list of standard cyber kill chains.

- [Lockheed Martin Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Unified Kill Chain](https://unifiedkillchain.com/)
- [Varonis Cyber Kill Chain](https://www.varonis.com/blog/cyber-kill-chain/)
- [Active Directory Attack Cycle](https://github.com/infosecn1nja/AD-Attack-Defense)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)

The Lockheed Martin kill chain focuses on a perimeter or external breach. Unlike other kill chains, it does not provide an in-depth breakdown of internal movement. You can think of this kill chain as a summary of all behaviors and operations present.

###### Components of the Martin Kill Chain

![image](https://github.com/MetricCode/Research/assets/99975622/cc9054c7-a55f-4c32-95ff-67e1b43c2068)


![image](https://github.com/MetricCode/Research/assets/99975622/4423e375-541f-4228-a46c-def761b51dfe)


