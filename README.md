# prediction-market-calibration

This project aims at estimating prediction market accuracy, since they have been repeatedly criticized for misrepresenting information due to biases such as the favourite-longshot or the preference bias. Especially with prediction market communities being increasingly operated with one stereotype of person. The question that begs to be asked is: **with what certainty can a prediction market calibrate the probability of specific events?**

This is especially interesting right now, since the discussion around implementing prediction markets into public policy making becomes increasingly sizeable and controversial.

## Scope

- Pull resolved binary markets from the Polymarket API and store their price history and final outcome
- Compute calibration curves and Brier scores over the full dataset
- Break calibration down by category, time-to-resolution, volume, and price bucket
- Predict outcomes from price-path features, using the market price itself as the baseline

## Hypotheses

- **Categories**: Multiple academic studies, such as the paper "Prediction Markets? The Accuracy and Efficiency of $2.4 Billion in the 2024 Presidential Election" by Joshua D. Clinton and TzuFeng Huang at Vanderbilt, established that accuracy varies by category. Public-speech-based prediction markets and sports markets are often cited to be among the least accurate.
- **Time-to-resolution**: It is a well documented phenomenon that markets with long resolution times are less accurate, since they present less incentive for competent traders to trade on. Capital locked in a long-dated contract cannot earn a return elsewhere, so traders discount distant markets.
- **Volume**: Likely the most important factor. More trade leads to more information flow in and out of the market.
- **Price buckets**: This is where the favourite-longshot bias would take place.

## Out of scope

- **One platform**: Polymarket only, since it is the only one that is big enough while also enabling access to past trading data.
- **No live data**: only markets that have already resolved.
- **No trading**: no automated or live execution. Any strategy is evaluated on paper against the market price.
