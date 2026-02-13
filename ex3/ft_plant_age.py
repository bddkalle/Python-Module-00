# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 12:41:00 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:19:30 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
