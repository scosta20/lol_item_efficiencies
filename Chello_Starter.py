import json
import pandas as pd

with open("items.json") as items_file:
    json_items = json.loads(items_file.read())

# Flatten the json like {"price": {"a": 1, "b": 3}} into "price.a": 1, "price.b": 3
items = pd.json_normalize(json_items).set_index(["id"])

# Now we basically have one massive excel table. Lots of NAs as we also flattened all the stats

# Note, all print statements only show the first 10 items by default
# Use items.head(X) to get first X items. Setting it to 99999999 will ensure you always print all...

# See columns and some items
print(items.columns)
print(items.head(5))

long_sword = items.loc[items.name=="Long Sword"]

# Check out long sword specifically
print(long_sword)

# Get everything long sword builds into
print(items.loc[long_sword.into])

# Copy as we're going to add a special column later..
dmg_items = items.loc[items["stats.FlatPhysicalDamageMod"]>0].copy()
# Find all flat physical damage items
print(dmg_items.head(35))

# Calc gold per damage

dmg_items["g_per_dmg"] = dmg_items["price.total"] / dmg_items["stats.FlatPhysicalDamageMod"]

print(dmg_items[["name", "g_per_dmg"]].head(30))

# Sort it, muramana sort of wrecks the calcs here.... Steraks probably also gets screwed
print(dmg_items.sort_values("g_per_dmg").head(12))
