{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO2KwBJs/UfdzsXntrzLs/W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/szasuz/a1/blob/main/Untitled0_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "18TGRSu7e0Jb",
        "outputId": "920149ae-ab6c-4202-86d6-eb29bbc7e437"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite valor em graus fareneit:50\n",
            "o valor de 50.0°F corresponde ao valor de 10.0°C\n"
          ]
        }
      ],
      "source": [
        "f =  float(input(\"digite valor em graus fareneit:\"))\n",
        "C = (5/9)*(f-32)\n",
        "print(f\"o valor de {f}°F corresponde ao valor de {C}°C\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "P = float(input(\"digite valor em polegadas: \"))\n",
        "MM = P * 25.4\n",
        "print(f\" o valor de {P}pol corresponde ao valor de {MM: .1f}MM\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aYhM-jrCjm3b",
        "outputId": "fc4b4f4a-9c4a-44af-fcb7-d532aad42ef5"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite valor em polegadas: 50\n",
            " o valor de 50.0pol corresponde ao valor de  1270.0MM\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "porgrama verificador de idade para votação\n"
      ],
      "metadata": {
        "id": "c50A0AhmpBVj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#entrada: idade\n",
        "#saida: \"pode votar ou não\"\n",
        "I= int(input(\"digite sua idade: \"))\n",
        "if I >= 18:\n",
        "  print(\"Pode votar\")\n",
        "else:\n",
        "    print(\"não pode votar\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NznvpE57pGZB",
        "outputId": "05ea2666-4deb-4405-d3dc-0e2212de8bfd"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite sua idade: 78\n",
            "Pode votar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "CONVERTER POLEGADA PARA MILIMETRO\n",
        "ENTRADA: P\n",
        "PROCESSAMENTO:\n",
        "MM = P* 25,4\n",
        "SAIDA: MM"
      ],
      "metadata": {
        "id": "xbtyyQJdj0gi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "entrada: f\n",
        "processamento: c=(5/9)(f-32)\n",
        "saida: c"
      ],
      "metadata": {
        "id": "Dpz9aTPsfBYl"
      }
    }
  ]
}