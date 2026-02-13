# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 12:58:49 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:19:13 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count(day) -> None:
        if day > days:
            return
        print(f"Day {day}")
        count(day + 1)
    count(1)
    print("Harvest time!")
