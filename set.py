#not in any particular order
#duplicates are not allowed
#cannot be modified - immutable
#no index, and therefore no accessing elements
Days=set(["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"])
Days.add("日曜日")
Days.discard("日曜日")
for d in Days:
    print(d)