# defining formatter as %r
formatter = "%s %s %s %s"
# prinint var calling the valiue 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
# calling strings
print formatter % ("one", "two", "three", "four")
# calling boolean, notice without ""
print formatter % (True, False, False, True)
# calling formatter with formatter print the original definition
print formatter % (formatter, formatter, formatter, formatter)
# print a string using , to keep it in one line but broken down for good practice
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
