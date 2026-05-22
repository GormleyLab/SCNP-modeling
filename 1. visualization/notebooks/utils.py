# Featurization funtions

# Charge features
def calc_charge(df, charge_dict=None):
    """Calculates and adds charge features columns to the dataframe, including total charge and net charge, based on individual monomer charges and polymer composition.
    
    Parameters: 
    df (pd.DataFrame): Polymer Composition dataframe.
    charge_dict (dict): Dictionary mapping monomer column names to their charge values. If none, default values will be used.
                'positive': list of positively charged monomer column names
                'negative': list of negatively charged monomer column names
                'zwitterionic': list of zwitterionic monomer column names
    Returns: 
    df updated with two new columns: 'Net Charge' and 'Total Charge'
    """
    
    # if no charge_dict provided, use default values
    if charge_dict is None:
        charge_dict = {
            'positive': ['TMAEMA'],
            'negative': ['SPMA'],
            'zwitterionic': ['SBMA']
        }
        print("No charge_dict provided, using default values.")
        
    # Only use columns that exist in the DataFrame
    positive_cols = [col for col in charge_dict['positive'] if col in df.columns]
    negative_cols = [col for col in charge_dict['negative'] if col in df.columns]
    zwitter_cols  = [col for col in charge_dict['zwitterionic']  if col in df.columns]
    
    # Calculate charge features: sum of positive, negative, and zwitterionic monomer fractions multiplied by DP
    pos_sum = df[positive_cols].sum(axis=1).fillna(0) * df['DP']
    neg_sum = df[negative_cols].sum(axis=1).fillna(0) * df['DP']
    zwit_sum = df[zwitter_cols].sum(axis=1).fillna(0) * df['DP']
    
    df['Net Charge'] = pos_sum - neg_sum  # Zwitterionic monomers contribute to total charge but not net charge, since they have both positive and negative charges that cancel out
    df['Total Charge'] = pos_sum + neg_sum + (2*zwit_sum)
    
    return df


# LogP feature
def calc_logP(df, monomer_columns=None, logP_dict=None):
    """Calculates and adds a LogP feature column to the dataframe, based on the monomer composition and their respective LogP values.
    
    Parameters: 
    df (pd.DataFrame): Polymer Composition dataframe.
    monomer_columns (list): List of monomer column names to include in the LogP calculation. If none, default values will be used.
    logP_dict (dict): Dictionary mapping monomer column names to their LogP values. If none, default values will be used.
    
    Returns: 
    df updated with a new column: 'LogP'
    """
    #if no monomer columns are provided, use default values
    if monomer_columns is None:
        monomer_columns = ['MMA', 'TMAEMA', 'DMAEMA', 'DMAPMA', 'SPMA', 'PEGMA', '2HPMA', 'TFEMA', 'BMA', 'SBMA', 'DMA']
        print(f"No monomer columns provided, using default columns: {monomer_columns}")

    #if no logP_dict is provided, use default values
    if logP_dict is None:
        # Default monomer LogP values
        logP_dict = {'MMA': 1.38, 'TMAEMA': -2.49, 'DMAEMA': 1.13, 'DMAPMA': 0.5, 'SPMA': -3.1, 'PEGMA': -1.2, '2HPMA': 0.97, 'TFEMA': 2.3, 'BMA': 3, 'SBMA': -4.23, 'DMA': 0.3}
        print(f"No LogP dictionary provided, using default values: {logP_dict}")

    # Calculate LogP : sum the LogP of each monomer multiplied by its weight in the polymer composition, then multiply the value by DP
    df['LogP'] = df.apply(
        lambda row: sum(logP_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1
    )
    
    return df
    
# Molecular weight feature
def calc_molecular_weight(df, monomer_columns=None, mw_dict=None):
    """Calculates and adds a Molecular Weight feature column to the dataframe, based on the monomer composition and their respective molecular weights.
    
    Parameters: 
    df (pd.DataFrame): Polymer Composition dataframe.
    monomer_columns (list): List of monomer column names to include in the molecular weight calculation. If none, default values will be used.
    mw_dict (dict): Dictionary mapping monomer column names to their molecular weights. If none, default values will be used.
    
    Returns: 
    df updated with two new columns: 'Molecular Weight (Da)' and 'Molecular Weight (kDa)'
    """
    #if no monomer columns are provided, use default values
    if monomer_columns is None:
        monomer_columns = ['MMA', 'TMAEMA', 'DMAEMA', 'DMAPMA', 'SPMA', 'PEGMA', '2HPMA', 'TFEMA', 'BMA', 'SBMA', 'DMA']
        print(f"No monomer columns provided, using default columns: {monomer_columns}")
        
    #if no molecular weight dictionary is provided, use default values
    if mw_dict is None:
        mw_dict = {'MMA': 100.12, 'TMAEMA': 171.24, 'DMAEMA': 157.21, 'DMAPMA': 170.25, 'SPMA': 246.32, 'PEGMA': 486.09, '2HPMA': 144.17, 'TFEMA': 168.11, 'BMA': 142.2, 'SBMA': 279.35, 'DMA': 99.13}
        print(f"No molecular weight dictionary provided, using default values: {mw_dict}")

    # Calculate molecular weight
    df['Molecular Weight (Da)'] = df.apply(
        lambda row: sum(mw_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1
    )
    # convert to kDa
    df['Molecular Weight (kDa)'] = df.apply(
        lambda row: sum(mw_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1)/1000  # Convert to kDa  # Convert to kDa

    return df

# Hydrogen Bonding features
def calc_hydrogen_bonding(df, monomer_columns=None, hbd_dict=None, hba_dict=None):
    """Calculates and adds Hydrogen Bond Donor (HBD), Hydrogen Bond Acceptor (HBA), Hydrogen Bond Total (HBT), and Hydrogen Bond Difference (HBDiff) feature columns to the dataframe, based on the monomer composition and their respective HBD and HBA values.
    
    Parameters: 
    df (pd.DataFrame): Polymer Composition dataframe.
    monomer_columns (list): List of monomer column names to include in the hydrogen bonding calculation. If none, default values will be used.
    hbd_dict (dict): Dictionary mapping monomer column names to their HBD values. If none, default values will be used.
    hba_dict (dict): Dictionary mapping monomer column names to their HBA values. If none, default values will be used.
    
    Returns: 
    df updated with five new columns: 'HBD', 'HBA', 'HBT' (Hydrogen Bond Total), 'HBDiff' (Hydrogen Bond Difference), and 'HBR' (Hydrogen Bonding Ratio)
    """
    #if no monomer columns are provided, use default values
    if monomer_columns is None:
        monomer_columns = ['MMA', 'TMAEMA', 'DMAEMA', 'DMAPMA', 'SPMA', 'PEGMA', '2HPMA', 'TFEMA', 'BMA', 'SBMA', 'DMA']
        print(f"No monomer columns provided, using default columns: {monomer_columns}")


        # if no HBD_dict is provided, use default values
    if hbd_dict is None:
        hbd_dict = {'MMA': 0, 'TMAEMA': 1, 'DMAEMA': 0, 'DMAPMA': 1, 'SPMA': 0, 'PEGMA': 1, '2HPMA': 1, 'TFEMA': 0, 'BMA': 0, 'SBMA': 0, 'DMA': 0}
        print(f"No donor dictionary provided, using default values: {hbd_dict}")
        
    # if no HBA_dict is provided, use default values
    if hba_dict is None:
        hba_dict = {'MMA': 2, 'TMAEMA': 3, 'DMAEMA': 3, 'DMAPMA': 2, 'SPMA': 5, 'PEGMA': 11, '2HPMA': 3, 'TFEMA': 5, 'BMA': 2, 'SBMA': 5, 'DMA': 1}
        print(f"No acceptor dictionary provided, using default values: {hba_dict}")
        
    # if no monomer_columns are provided, use default values
    if monomer_columns is None:
        monomer_columns = ['MMA', 'TMAEMA', 'DMAEMA', 'DMAPMA', 'SPMA', 'PEGMA', '2HPMA', 'TFEMA', 'BMA', 'SBMA', 'DMA']
        print(f"No monomer columns provided, using default columns: {monomer_columns}")


    # Calculate H-bond donors and acceptors: sum the H-bond donor/acceptor counts of each monomer multiplied by its weight in the polymer composition, then multiply the value by DP
    donor_total = df.apply(lambda row: sum(hbd_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1)
    acceptor_total = df.apply(lambda row: sum(hba_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1)

    df['HBD'] = donor_total
    df['HBA'] = acceptor_total
    df['HBT'] = donor_total + acceptor_total
    df['HBDiff'] = donor_total - acceptor_total
    df['HBR'] = df['HBD']/df['HBA']
    
    return df

# Surface Area feature
def calc_surface_area(df, monomer_columns=None, area_dict=None):
    """Calculates and adds a Surface Area feature column to the dataframe, based on the monomer composition and their respective surface area values.
    
    Parameters: 
    df (pd.DataFrame): Polymer Composition dataframe.
    monomer_columns (list): List of monomer column names to include in the surface area calculation. If none, default values will be used.
    area_dict (dict): Dictionary mapping monomer column names to their surface area values. If none, default values will be used.
    
    Returns: 
    df updated with a new column: 'Surface Area (Å²)'
    """
       #if no monomer columns are provided, use default values
    if monomer_columns is None:
        monomer_columns = ['MMA', 'TMAEMA', 'DMAEMA', 'DMAPMA', 'SPMA', 'PEGMA', '2HPMA', 'TFEMA', 'BMA', 'SBMA', 'DMA']
        print(f"No monomer columns provided, using default columns: {monomer_columns}")
        
    #if no surface area dictionary is provided, use default values
    if area_dict is None:
        area_dict = {'MMA': 26.3, 'TMAEMA': 52.3, 'DMAEMA': 29.5, 'DMAPMA': 32.2, 'SPMA': 91.9, 'PEGMA': 120, '2HPMA': 46.5, 'TFEMA': 26.3, 'BMA': 26.3, 'SBMA': 91.9, 'DMA': 20.3}
        print(f"No surface area dictionary provided, using default values: {area_dict}")

    # Calculate surface area: sum the surface area of each monomer multiplied by its weight in the polymer composition, then multiply the value by DP
    df['Surface Area (Å²)'] = df.apply(lambda row: sum(area_dict.get(monomer, 0) * row[monomer] for monomer in monomer_columns) * row['DP'], axis=1)

    return df

# Neutral monomer fraction feature
def calc_neutral_fraction(df, neutral_monomers=None):
    """Calculates the sum of the neutral monomer fractions for each polymer composition in a dataframe, based on a list of neutral monomers.

    Parameters:
    df (pd.DataFrame): DataFrame containing the polymer compositions.
    neutral_monomers (list): List of neutral monomers. If None, default values are used.

    Returns:
    df with a new column 'Neutral_Fraction'.
    """
    
    #if no monomer columns are provided, use default values
    if neutral_monomers is None:
        neutral_monomers = ['2HPMA','DMA']
        print(f"No monomer columns provided, using default columns: {neutral_monomers}")

    # Calculate neutral fraction: sum the fractions of the neutral monomers in the polymer composition
    df['Neutral Fraction'] = df.apply(lambda row: sum(row[monomer] for monomer in neutral_monomers if monomer in row), axis=1)

    return df

# Function to apply all featurization functions to a dataframe
def featurize(df, charge_dict=None, logP_dict=None, mw_dict=None, hbd_dict=None, hba_dict=None, area_dict=None, neutral_monomers=None):
    """Applies all featurization functions to a polymer composition dataframe to calculate and add chemical features based on the monomer composition and properties.

    Parameters:
    df (pd.DataFrame): Polymer Composition dataframe.
    charge_dict (dict): Dictionary mapping monomer column names to their charge values. If none, default values will be used.
    logP_dict (dict): Dictionary mapping monomer column names to their LogP values. If none, default values will be used.
    mw_dict (dict): Dictionary mapping monomer column names to their molecular weights. If none, default values will be used.
    hbd_dict (dict): Dictionary mapping monomer column names to their HBD values. If none, default values will be used.
    hba_dict (dict): Dictionary mapping monomer column names to their HBA values. If none, default values will be used.
    area_dict (dict): Dictionary mapping monomer column names to their surface area values. If none, default values will be used.
    neutral_monomers (list): List of neutral monomers. If none, default values are used.
    
    Returns:
    df updated with new feature columns: 'Net Charge', 'Total Charge', 'LogP', 'Molecular Weight (kDa)', 'HBD', 'HBA', 'HBT', 'HBDiff', 'Surface Area (Å²)', and 'Neutral Fraction'
    """
    
    df = calc_charge(df, charge_dict)
    df = calc_logP(df, logP_dict)
    df = calc_molecular_weight(df, mw_dict)
    df = calc_hydrogen_bonding(df, hbd_dict, hba_dict)
    df = calc_surface_area(df, area_dict)
    df = calc_neutral_fraction(df, neutral_monomers)
    
    return df