from Utils.Offsets import *
import time



def SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager, entity_glow, eteam) :

    if entity_hp > 50 and not entity_hp == 100:
        r, g, b = 255, 165, 0
    elif entity_hp < 50:
        r, g, b = 255, 0, 0
    elif entity_hp == 100 and entity_team_id == 2:
        r, g, b = 0, 255, 0
    else:
        r, g, b = 0, 255, 0



    if entity_team_id == 2:  # Terrorist
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

    elif entity_team_id == 3:  # Counter-terrorist
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow


def GetEntityVars(pm, entity):
    while True:
        try:
            entity_glow = pm.read_uint( entity + m_iGlowIndex )

            entity_team_id = pm.read_uint( entity + m_iTeamNum )
            entity_isdefusing = pm.read_uint( entity + m_bIsDefusing )
            entity_hp = pm.read_uint( entity + m_iHealth )
            entity_dormant = pm.read_uint( entity + m_bDormant )
        except:
            print( "Could not load Players Infos (Should only do this once)" )
            time.sleep( 0.2 )
            continue
        return entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant

