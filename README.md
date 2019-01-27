
# Insite Backend

The backend powering Insite, the Chrome extension that helps you make informed decisions on articles. 
 
Get the real Insite on things!

Download here: https://chrome.google.com/webstore/detail/insite/kalaoonpgfodfdoleffjbchodofdmgno?hl=en

Learn more here: https://devpost.com/software/nwhacks2019_frontend

The actual code for the Chrome extension can be found here: https://github.com/farisfizal/nwhacks2019_frontend

## Inspiration
We wanted to have a quick and simple way of determining if something was likely to be fake news or not. Many existing services take too long, and need you to copy and paste the url into a separate web page. Insite allows you to do this in the browser, without ever leaving the page.

## What it does
Key features: 
- Fake news analysis in percentage
- Summarize long articles to a fraction of their size
- Helps people make informed decisions about what they're reading

## How we built it
Used a Python Flask backend that called the required APIs and dealt with required authentication for said APIs. The backend also parsed and returned the data from the APIs into a simple format so that the frontend could easily use it.

We made a chrome extension with a popup that would appear when you clicked on the icon. From there, we used jquery to simply call the Python backend, and displayed the data it returned.

## Challenges we ran into
As a result of a lack of foresight, we initially rushed into the project without enough planning. As a result, we began developing the Chrome extension as a tooltip that would appear when the mouse hovered above a valid link. This, however, proved to be extremely difficult given our inexperience with web extensions. We struggled to get the tooltip to appear in the first place. Once we were able to implement a dummy tooltip, we were unable to modify our extension to call the API's used in our project. This problem persisted, and thus, we decided to take a more streamlined approach that alleviates the need for a tooltip. Our team now realizes that we spent too much time trying to develop the tooltip functionality, which distracted us from the bigger picture. In the future, we will come together as a team periodically and discuss our progress to ensure that we stay on track throughout the hackathon.

## Accomplishments that we're proud of
We're proud that we pivoted away from trying to directly fix the problem, as the potential solutions that we tried to implement didn't work. Instead, a more simple and easier implementation was used, which completely avoided the issues that we had with the flood of server requests with the back end. Finding this simplicity was key to being able to deliver our project.

## What we learned
Never underestimate a task, no matter how easy it _seems_. If you are running into trouble, either pivot the idea, or try to simplify things, as making things more complex than they need to be is never good. Never spend more than 1 hour doing something if you aren't making progress.
Break down problems, and discuss constantly with team mates about any blocking challenges or issues.

## What's next for Insite
Performance improvements on the backend, as well as displaying more metrics to help people make an informed decision.
