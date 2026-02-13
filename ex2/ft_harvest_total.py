# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 12:32:53 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:18:28 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total() -> None:
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day1 + day2 + day3}")
