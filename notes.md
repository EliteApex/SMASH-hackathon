# Gravitational waves 
Gravitational waves (GWs) are ripples in sapce time caused by the acceleration of massive objects. The way to detect GWs is to measure the speed of light. If the space is squeezed, light takes less time to travel a distance, and if it is stretched, it takes more. 
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/The_Gravitational_wave_spectrum_Sources_and_Detectors.jpg"> 

There are a number of characteristics used to describe a gravitational wave:
**Amplitude**: Usually denoted h, the size of the wave – the fraction of stretching or squeezing.
**Frequency**: Usually denoted f, the frequency with which the wave oscillates (1 divided by the amount of time between two successive maximum stretches or squeezes)
**Wavelength**: Usually denoted λ, this is the distance along the wave between points of maximum stretch or squeeze.
**Speed**: This is the speed at which a point on the wave (for example, a point of maximum stretch or squeeze) travels. For gravitational waves with small amplitudes, this wave speed is equal to the speed of light \(c\).

<span style="color:red">\(**Understanding: What was our data measuring from the above? )* </span>.

### Known GW sources: Compact Binary Inspiral Gravitational Waves with matched-filtering 
So far, all objects LIGO has detected falls into this category. Those waves are produced by orbiting pairs of massive and dense objects. **Matched filtering** here is a process used to enlarge the signal-to-noise ratio. 
- BBH mergers: two black holes. Detectable during final moments of the merger. 
- BNS mergers: two neutron stars. Emit gravitational waves as they orbit and merge. Followed by electromagnetic signals in the full spectrum, including gamma-ray bursts. 
- BHNS mergers: A blackhole and a neutron star. Potentially creates a variaety of electromagnetic emissions. 

For all three, the mechanism of wave-generation is the same: **inspiral**.
- This process occurs over millions of years. As two dense objects orbit each other, they radiate gravitational waves that carries way some of the system's orbital energy. This cause them to be closer together, the closer they are, the faster they orbit. The faster they are, the more waves they radiate, and the system loses more energy, by the conservation of angular momentum.
- LIGO only cataches the last few orbits before the collision. The time the objects spend orbiting and emiting waves in LIGO's range is typically **a fraction of a second to tens of seconds**, depending on the mass of the object. 
	- The more massive an object, the faster it moves through the final phase. The first blackholes (BBH) mergers' waves lasted two-tenths of a second, and the first neutron start mergers lasted over 100 seconds. 

# LIGO 
 The laser Interferometer Gravitaional-wave Observatory (LIGO) has two stations, allowing for verification of signals: Hanford, Washinton and Livington, Louisiana. Both stations consist of two tubes stretching 4 kilometers perpendicularly. 
 When gravitational wave passes through, it stretches the space in  one direction and squeezes space in the other.  A laser beam from a single source is split in half. Each beam travels down an arm perpendicular to the other, bounces off a mirror at the end, and returns (ultimately) to be reunited ("interfered") with its partner. By studying how the beams interfere, we can determine if a gravitational wave has passed. 
 
In the stations, the lasers are set to 1 megawatt each, enough power to support 1000 households. This is to reduce possible noise, for the more photons there are, the more the possibility of true detection. 

<img src="https://qph.cf2.quoracdn.net/main-qimg-7e07751be612500e77e4484eb4bcfe71.webp" height="1000">
 
<img src="https://www.ligo.caltech.edu/system/pages/images/27/page/ifoschematic.jpg" height="300">


# Problem statement 

# Dataset 
### Strain (*h*) 

The individual numbers in the dataset are most likely strain measurements- A dimensionless quantity representing relative change in length (Δ𝐿/𝐿). 

Δ𝐿: The change in the interferometer arm length due to a gravitational wave.
𝐿: The original length of the interferometer arm.

> Gravitational wave interferometric detectors are the most sensitive position meters in existence, aiming to measure strain (∆L/L) sensitivities of the order of 10-23. 
> src:  [LIGO R&D](https://www.ligo.caltech.edu/page/research-development?highlight=strain) 

Each pair of numbers in the last dimension corresponds to simultaneous strain measurements from Hanford Detector (first number) and  Livingston Detector (second number).

- Binaries **(simulated)**: gravitational waves expected from Binary Black Holes (BBH). **Injected into real background noise** to help train the models. ***(Positives)*** 
- Background **(Actual)**: Background noise from the O3a observation period. Any known gravitational wave events and other excess power glitches have been removed from this data. This "cleaned" background noise is what participants will primarily use to train their models to detect anomalies. ***(Negatives)***  
- Sine-Gaussian **(simulated)**: Generic low-frequency signals used to represent potential gravitational wave sources that do not fit into the well-understood categories like BBH. ***(Positives)*** 
 
 
