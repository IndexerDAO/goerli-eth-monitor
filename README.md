# goerli-eth-monitor

Monitor your testnet Indexer Operator wallet ETH balance

## Getting Started

1. Fork the repo
2. Create a [Discord webook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for a channel of your liking.
3. In your newly created GitHub repository, Navigate to Settings -> Secrets -> Actions
4. Create two new repository secrets
    * `OPERATOR_ADDRESS` = Indexer Operator wallet address on Goerli Testnet
    * `WEBHOOK_URL` = Discord channel Webhook URL 
5. You're good to go

## Modifying notification schedule
The tool is currently set to an hourly timer, configured in [`.github/workflows/app.yml`](https://github.com/IndexerDAO/goerli-eth-monitor/blob/main/.github/workflows/app.yml)

``` yaml
on:
  schedule:
     - cron:  '0 * * * *'
```

Update the `cron` expression according to your needs. 
* This is a helpful tool for cron expression building: https://crontab.guru/
