# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 12:58:49 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:19:06 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
