# XDhacksCOVID-project

## Overview
The following project was created for the XDhacksCOVID Hackathon and made by team Ctrl+Alt+Elite. The code demostrates viable structures for implementing our idea of a COVID related application

### Map
The mapping software makes use of Google's Javascript Map API and will allow the user to take preventative measures against COVID-19 through avoiding high density and risk areas. In addition it includes a search feature that allows users to plan their route. The webpage includes the majority of google maps functionality including location data, street view, satellite view, terrain view, bus routes, traffic levels, zoom, and autcomplete address search.

### Case Estimater
The COVID case estimator uses a simple exponential formula, a set of known deaths related to COVID, and a few assumptions about the transmition of the pandemic to approximate the number of infected people in a given population. This process was inspired by a Khan Academy Video on the same idea of approximating the cases in a given population due to inherently inaccurate testing with accurate death numbers.

### Contact Tracing Algorithm 
The contact tracing algorithym queries through a list of GPS co-ordinates aquired by some means wheather this is LTE/Cellular or Bluetooth data in order to keep remind induviduals about social distancing measures depending on their proximity and also let them know if they have been in contact with someone that is caring the disease. The algorithym uses a simple query that will not double count (i'm pretty sure its n^2 but idk)

##References
