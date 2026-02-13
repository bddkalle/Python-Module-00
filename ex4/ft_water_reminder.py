# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 12:51:48 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:19:25 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
