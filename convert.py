import pandas as pd


class Convert:
    """
    A class used to convert ISO-3166 alpha-2 codes.

    This class can be used to convert country codes to continent codes, which can then be further converted into
    full continent names. The data was taken from wikipedia:
    https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)

    Methods
    -------
    to_continent_code(country: str)
        Converts country code to continent code

    to_continent_name(code: str)
        Converts continent code to continent name

    map_to_continent_code(df: pd.DataFrame)
        Maps continent codes to visitor_country

    map_to_continent_name(df: pd.DataFrame)
        Maps continent names to visitor_country

    """

    def __init__(self):
        self._country_to_continent = {
            'AB': 'AS',
            'AD': 'EU',
            'AE': 'AS',
            'AF': 'AS',
            'AG': 'NA',
            'AI': 'NA',
            'AL': 'EU',
            'AM': 'AS',
            'AO': 'AF',
            'AR': 'SA',
            'AS': 'OC',
            'AT': 'EU',
            'AU': 'OC',
            'AW': 'NA',
            'AX': 'EU',
            'AZ': 'AS',
            'BA': 'EU',
            'BB': 'NA',
            'BD': 'AS',
            'BE': 'EU',
            'BF': 'AF',
            'BG': 'EU',
            'BH': 'AS',
            'BI': 'AF',
            'BJ': 'AF',
            'BL': 'NA',
            'BM': 'NA',
            'BN': 'AS',
            'BO': 'SA',
            'BQ': 'NA',
            'BR': 'SA',
            'BS': 'NA',
            'BT': 'AS',
            'BV': 'AN',
            'BW': 'AF',
            'BY': 'EU',
            'BZ': 'NA',
            'CA': 'NA',
            'CC': 'AS',
            'CD': 'AF',
            'CF': 'AF',
            'CG': 'AF',
            'CH': 'EU',
            'CI': 'AF',
            'CK': 'OC',
            'CL': 'SA',
            'CM': 'AF',
            'CN': 'AS',
            'CO': 'SA',
            'CR': 'NA',
            'CU': 'NA',
            'CV': 'AF',
            'CW': 'NA',
            'CX': 'AS',
            'CY': 'AS',
            'CZ': 'EU',
            'DE': 'EU',
            'DJ': 'AF',
            'DK': 'EU',
            'DM': 'NA',
            'DO': 'NA',
            'DZ': 'AF',
            'EC': 'SA',
            'EE': 'EU',
            'EG': 'AF',
            'ER': 'AF',
            'ES': 'EU',
            'ET': 'AF',
            'FI': 'EU',
            'FJ': 'OC',
            'FK': 'SA',
            'FM': 'OC',
            'FO': 'EU',
            'FR': 'EU',
            'GA': 'AF',
            'GB': 'EU',
            'GD': 'NA',
            'GE': 'AS',
            'GF': 'SA',
            'GG': 'EU',
            'GH': 'AF',
            'GI': 'EU',
            'GL': 'NA',
            'GM': 'AF',
            'GN': 'AF',
            'GP': 'NA',
            'GQ': 'AF',
            'GR': 'EU',
            'GS': 'SA',
            'GT': 'NA',
            'GU': 'OC',
            'GW': 'AF',
            'GY': 'SA',
            'HK': 'AS',
            'HM': 'AN',
            'HN': 'NA',
            'HR': 'EU',
            'HT': 'NA',
            'HU': 'EU',
            'ID': 'AS',
            'IE': 'EU',
            'IL': 'AS',
            'IM': 'EU',
            'IN': 'AS',
            'IO': 'AS',
            'IQ': 'AS',
            'IR': 'AS',
            'IS': 'EU',
            'IT': 'EU',
            'JE': 'EU',
            'JM': 'NA',
            'JO': 'AS',
            'JP': 'AS',
            'KE': 'AF',
            'KG': 'AS',
            'KH': 'AS',
            'KI': 'OC',
            'KM': 'AF',
            'KN': 'NA',
            'KP': 'AS',
            'KR': 'AS',
            'KW': 'AS',
            'KY': 'NA',
            'KZ': 'AS',
            'LA': 'AS',
            'LB': 'AS',
            'LC': 'NA',
            'LI': 'EU',
            'LK': 'AS',
            'LR': 'AF',
            'LS': 'AF',
            'LT': 'EU',
            'LU': 'EU',
            'LV': 'EU',
            'LY': 'AF',
            'MA': 'AF',
            'MC': 'EU',
            'MD': 'EU',
            'ME': 'EU',
            'MF': 'NA',
            'MG': 'AF',
            'MH': 'OC',
            'MK': 'EU',
            'ML': 'AF',
            'MM': 'AS',
            'MN': 'AS',
            'MO': 'AS',
            'MP': 'OC',
            'MQ': 'NA',
            'MR': 'AF',
            'MS': 'NA',
            'MT': 'EU',
            'MU': 'AF',
            'MV': 'AS',
            'MW': 'AF',
            'MX': 'NA',
            'MY': 'AS',
            'MZ': 'AF',
            'NA': 'AF',
            'NC': 'OC',
            'NE': 'AF',
            'NF': 'OC',
            'NG': 'AF',
            'NI': 'NA',
            'NL': 'EU',
            'NO': 'EU',
            'NP': 'AS',
            'NR': 'OC',
            'NU': 'OC',
            'NZ': 'OC',
            'OM': 'AS',
            'OS': 'AS',
            'PA': 'NA',
            'PE': 'SA',
            'PF': 'OC',
            'PG': 'OC',
            'PH': 'AS',
            'PK': 'AS',
            'PL': 'EU',
            'PM': 'NA',
            'PR': 'NA',
            'PS': 'AS',
            'PT': 'EU',
            'PW': 'OC',
            'PY': 'SA',
            'QA': 'AS',
            'RE': 'AF',
            'RO': 'EU',
            'RS': 'EU',
            'RU': 'EU',
            'RW': 'AF',
            'SA': 'AS',
            'SB': 'OC',
            'SC': 'AF',
            'SD': 'AF',
            'SE': 'EU',
            'SG': 'AS',
            'SH': 'AF',
            'SI': 'EU',
            'SJ': 'EU',
            'SK': 'EU',
            'SL': 'AF',
            'SM': 'EU',
            'SN': 'AF',
            'SO': 'AF',
            'SR': 'SA',
            'SS': 'AF',
            'ST': 'AF',
            'SV': 'NA',
            'SY': 'AS',
            'SZ': 'AF',
            'TC': 'NA',
            'TD': 'AF',
            'TG': 'AF',
            'TH': 'AS',
            'TJ': 'AS',
            'TK': 'OC',
            'TM': 'AS',
            'TN': 'AF',
            'TO': 'OC',
            'TP': 'AS',
            'TR': 'AS',
            'TT': 'NA',
            'TV': 'OC',
            'TW': 'AS',
            'TZ': 'AF',
            'UA': 'EU',
            'UG': 'AF',
            'US': 'NA',
            'UY': 'SA',
            'UZ': 'AS',
            'VC': 'NA',
            'VE': 'SA',
            'VG': 'NA',
            'VI': 'NA',
            'VN': 'AS',
            'VU': 'OC',
            'WF': 'OC',
            'WS': 'OC',
            'XK': 'EU',
            'YE': 'AS',
            'YT': 'AF',
            'ZA': 'AF',
            'ZM': 'AF',
            'ZW': 'AF',
        }

        self._code_to_continent = {
            'AF': 'Africa',
            'AS': 'Asia',
            'NA': 'North America',
            'EU': 'Europe',
            'SA': 'South America',
            'OC': 'Oceania',
            'AN': 'Antarctica'
        }

    def to_continent_code(self, country: str) -> str:
        """

        Parameters
        ----------
        country: str
            The two letter ISO-3166 country code

        Raises
        ------
        KeyError
            If input country is not in ISo-3166 format or does not exist in the dictionary

        Returns
        -------
        str
            The two letter continent code
        """

        if (country is None) or (len(country) != 2):
            raise KeyError("Invalid ISO3166 alpha-2 country code.")

        if country not in self._country_to_continent:
            raise KeyError("Country code not recognized.")

        return self._country_to_continent[country]

    def to_continent_name(self, code: str) -> str:
        """

        Parameters
        ----------
        code: str
            Two letter ISO-3166 continent code

        Raises
        ------
        KeyError
            If input continent is not in ISo-3166 format or does not exist in the dictionary

        Returns
        -------
        str
            The full name of the continent

        """
        if (code is None) or (len(code) != 2):
            raise KeyError("Invalid ISO3166 alpha-2 continent code.")

        if code not in self._code_to_continent:
            raise KeyError("Continent code not recognized.")

        return self._code_to_continent[code]

    def map_to_continent_code(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert country code to continent code

        Take a dataframe and map the country_to_continent code dictionary on its 'visitor_country' column.
        Afterwards, map the code_to_continent name dictionary on 'visitor_country'.

        Parameters
        ----------
        df: pd.DataFrame
            Dataframe where country codes need to be converted into continent codes and then later into names

        Returns
        -------
        name_df: pd.DataFrame
            Dataframe where country codes have been replaced with continent names

        """
        # Map the dictionary to replace values
        series = df.visitor_country.map(self._country_to_continent)

        # Map results in a series, so convert into DataFrame, convert continent codes to names and return it
        code_df = pd.DataFrame(series).reset_index()
        code_df.columns = ['index', 'visitor_country']
        return self.map_to_continent_name(code_df)

    def map_to_continent_name(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert continent code to continent name

        Take a series, convert it to dataframe and map the code_to_continent name dictionary on its
        'visitor_country' column.

        Parameters
        ----------
        df: pd.DataFrame
            DataFrame where continent codes need to be converted into continent names

        Returns
        -------
        df: pd.DataFrame
            Dataframe where continent codes have been replaced with continent names

        """
        # Map returns a series
        series = df.visitor_country.map(self._code_to_continent)

        # Convert series to df and return it
        name_df = pd.DataFrame(series).reset_index()
        name_df.columns = ['index', 'visitor_country']
        return name_df
