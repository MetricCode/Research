### CIA Triad

#### Confidentiality

- This element is the protection of data from unauthorized access and misuse. 
- Confidentiality is to protect this data from parties that it is not intended for.

#### Integrity

- Integrity is the condition where information is kept accurate and consistent unless authorized changes are made. 
- It is possible for the information to change because of careless access and use, errors in the information system, or unauthorized access and use. 
- Integrity is maintained when the information remains unchanged during storage, transmission, and usage not involving modification to the information. Steps must be taken to ensure data cannot be altered by unauthorised people.

#### Availability

- In order for data to be useful, it must be available and accessible by the user.

### Principles of Priviledges

The levels of access given to individuals are determined on two primary factors:
-   The individual's role/function within the organisation
-   The sensitivity of the information being stored on the system

Two key concepts are used to assign and manage the access rights of individuals, two key concepts are used: 
- Privileged Identity Management (PIM) - PIM is used to translate a user's role within an organisation into an access role on a system.
- Privileged Access Management (PAM) - PAM is the management of the privileges a system's access role has, amongst other things.

Simply, users should be given the minimum amount of privileges, and only those that are absolutely necessary for them to perform their duties. Other people should be able to trust what people write to.

### Security Models
According to a security model, any system or piece of technology storing information is called an information system, which is how we will reference systems and devices in this task.

#### Security Models used to achieve the CIA Triad
##### The Bell-La Padula Model

 - Is used to achieve confidentiality. This model has a few assumptions, such as an organisation's hierarchical structure it is used in, where everyone's responsibilities/roles are well-defined.
 - The model works by granting access to pieces of data (called objects) on a strictly need to know basis. This model uses the rule "no write down, no read up".
**Advantages**

- Policies in this model can be replicated to real-life organisations hierarchies (and vice versa)
- Simple to implement and understand, and has been proven to be successful.

- Disadvantages
- Even though a user may not have access to an object, they will know about its existence - so it's not confidential in that aspect.
- The model relies on a large amount of trust within the organisation.


![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/0e6e5d9d80785fc287b4a67e1453b295.png)

The Bell LaPadula Model is popular within organisations such as governmental and military because members of the organisations are presumed to have already gone through a process called vetting. 

Vetting is a screening process where applicant's backgrounds are examined to establish the risk they pose to the organisation. Therefore, applicants who are successfully vetted are assumed to be trustworthy - which is where this model fits in.

##### Biba Model
- Is used to achieve integrity.
- It applies the rule to objects (data) and subjects (users) that can be summarised as "no write up, no read down". This rule means that subjects **can** create or write content to objects at or below their level but **can only** read the contents of objects above the subject's level.

**Advantages**
- Simple to implement
- Resolves the limitations of the Bell-La Padula model by addressing both confidentiality and data integrity.

**Disadvantages**
- There will be many levels of access and objects. Things can be easily overlooked when applying security controls.
- Often results in delays within a business. For example, a doctor would not be able to read the notes made by a nurse in a hospital with this model.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/895ba351ef24ef6495d290222e49470e.png)

The Biba model is used in organisations or situations where integrity is more important than confidentiality. 

For example, in software development, developers may only have access to the code that is necessary for their job. They may not need access to critical pieces of information such as databases, etc.

### Threat Modelling & Incident Response
  
Threat modelling is the process of reviewing, improving, and testing the security protocols in place in an organisation's information technology infrastructure and services.

A critical stage of the threat modelling process is identifying likely threats that an application or system may face, the vulnerabilities a system or application may be vulnerable to.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5de96d9ca744773ea7ef8c00/room-content/aabdd83977336fd44b3645a86e5ba20e.png)  

The threat modelling process is very similar to a risk assessment made in workplaces for employees and customers. The principles all return to:

-   Preparation
-   Identification
-   Mitigations
-   Review

An effective threat model includes:

-   Threat intelligence
-   Asset identification
-   Mitigation capabilities
-   Risk assessment

![Screenshot from 2023-04-16 17-33-52](https://user-images.githubusercontent.com/99975622/232320244-079a4c3a-31c4-41c5-beb2-1bed96fc3a98.png)


A breach of security is known as an incident.

Incidents are classified using a rating of urgency and impact. Urgency will be determined by the type of attack faced, where the impact will be determined by the affected system and what impact that has on business operations.

![Screenshot from 2023-04-16 17-38-41](https://user-images.githubusercontent.com/99975622/232320517-25ba895c-c66f-4c20-8571-8199298f2582.png)
