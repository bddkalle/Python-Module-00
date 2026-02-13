# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fschnorr <fschnorr@student.42berlin.de>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/11 11:43:21 by fschnorr            #+#    #+#            #
#   Updated: 2026/02/13 14:18:49 by fschnorr           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
