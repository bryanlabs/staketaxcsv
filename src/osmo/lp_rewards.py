
from osmo import api_data
from osmo.make_tx import make_lp_reward_tx


def lp_rewards(wallet_address, reward_tokens, exporter, progress):
    for i, token in enumerate(reward_tokens):
        message = "Retrieving lp rewards for token={}".format(token)
        progress.report(lp_rewards.__name__, i, message)

        elems = api_data.get_lp_rewards(wallet_address, token)
        for elem in elems:
            day = elem["day"]
            amount = elem["amount"]
            row = make_lp_reward_tx(wallet_address, day, amount, token)
            exporter.ingest_row(row)
