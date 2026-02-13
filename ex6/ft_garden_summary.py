# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 13:45:51 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:15:47 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_summary() -> None:
    name = input("Enter garden name: ")
    plants = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {plants}")
    print("Status: Growing well!")
