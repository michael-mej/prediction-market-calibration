# prediction-market-calibration

This project aims at estimating prediction market accuracy, since they have been repeatedly criticized for misrepresenting information due to biases such as the favourite-longshot or the preference bias. Especially with prediction market communities being increasingly operated with one stereotype of person. The question that begs to be asked is: **with what certainty can a prediction market calibrate the probability of specific events?**

This is especially interesting right now, since the discussion around implementing prediction markets into public policy making becomes increasingly sizeable and controversial.

The project answers this from inside the market rather than from a dataset. Every forecast is written down before the market price is looked at, and both are scored against the same outcomes.

## Scope

- Log a probability and a short written rationale for each macro release, recorded **before** the market price is consulted
- Record the market price at decision time, the direction taken, the size, and the settled outcome — including decisions not to trade
- Compute calibration curves and Brier scores for two forecasters over the same events: the market, and me
- Break calibration down by category, time-to-resolution, and liquidity
- Measure realised edge against the market price, net of fees

## Hypotheses

- **Categories**: Multiple academic studies, such as the paper "Prediction Markets? The Accuracy and Efficiency of $2.4 Billion in the 2024 Presidential Election" by Joshua D. Clinton and TzuFeng Huang at Vanderbilt, established that accuracy varies by category. Public-speech-based prediction markets and sports markets are often cited to be among the least accurate.
- **Liquidity**: Likely the most important factor. More trade leads to more information flow in and out of the market. Thinly traded contracts should show both larger calibration errors and wider spreads.
- **Price buckets**: This is where the favourite-longshot bias would take place.
- **Time-to-resolution**: Long-dated contracts are usually held to be less accurate, since capital locked in them cannot earn a return elsewhere and competent traders stay away. ForecastEx pays a coupon on held contracts, which removes that disincentive, so the usual decay in accuracy with horizon should be weaker here than on venues without one.
- **Scheduled releases**: Where a settlement figure is partly published before expiry, such as monthly GDP components within a quarter, prices should track the incoming data. Any lag is a measurable edge.

## Out of scope

- **One venue**: ForecastEx via IBKR only.
- **No automation**: Decided to settle on no API, no execution code. Decisions are made and logged by hand.
- **No discretionary non-macro trading**: contracts settling on announcements rather than published data are excluded, since they cannot be priced against a public series.
