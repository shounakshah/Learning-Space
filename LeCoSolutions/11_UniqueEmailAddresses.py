# Every email consists of a local name and a domain name, separated by the @ sign.
#
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
#
# Besides lowercase letters, these emails may contain '.'s or '+'s.
#
# If you add periods ('.') between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.
# (Again, this rule does not apply for domain names.)
#
# It is possible to use both of these rules at the same time.
#
# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails?
#
#
#
# Example 1:
#
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#
#
# Note:
#
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.
#
#
#
# Runtime: 44 ms
# Beats: 99.33%

emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

# Will be used to find unique email addresses
unique_email_address_set = set()

# For every email address:
for current_email in emails:
    #   Split it at @
    local, domain = current_email.split('@')
    # print(local)

    #   Find + in the string and truncate the string after +
    local = local[0:local.find('+')]
    # print(local)

    #   Replace all the .s in the string
    local = local.replace('.', '')
    # print(local)

    #   Merge the split strings
    merged_email = local + "@" + domain
    # print(merged_email)

    #   Add the merged string to a set to find all unique addresses
    unique_email_address_set.add(merged_email)

print(f"Total number of unique email addresses in {unique_email_address_set} is: {len(unique_email_address_set)}")
