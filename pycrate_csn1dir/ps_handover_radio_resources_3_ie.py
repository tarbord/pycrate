# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/ps_handover_radio_resources_3_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.42b PS Handover Radio Resources 3
# top-level object: PS Handover Radio Resources 3 IE

# external references
from pycrate_csn1dir.pulse_format_ie import dlmc_frequency_parameters_ie
from pycrate_csn1dir.global_packet_timing_advance_ie import global_packet_timing_advance_ie
from pycrate_csn1dir.dynamic_allocation_3_ie import dynamic_allocation_3_ie
from pycrate_csn1dir.pulse_format_ie import pulse_format_ie
from pycrate_csn1dir.power_control_parameters_ie import power_control_parameters_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.egprs_modulation_and_coding_scheme_ie import egprs_modulation_and_coding_scheme_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

rlc_entity_struct = CSN1List(name='rlc_entity_struct', list=[
  CSN1Bit(name='tfi', bit=5),
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='pfi', bit=7)])

ccn_support_description_struct = CSN1List(name='ccn_support_description_struct', list=[
  CSN1Bit(name='number_cells', bit=7),
  CSN1Bit(name='ccn_supported', num=([0], lambda x: x))])

additional_pfcs_struct = CSN1List(name='additional_pfcs_struct', list=[
  CSN1Bit(name='tfi', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='pfi', bit=7)])

dlmc_ul_carrier_info_struct = CSN1Alt(name='dlmc_ul_carrier_info_struct', alt={
  '00': ('', []),
  '01': ('', []),
  '10': ('', [
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='uplink_timeslot_allocation', bit=8)])})]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='uplink_pdch_pairs_dlmc', bit=8)])})])}),
  CSN1Ref(name='dynamic_allocation_3', obj=dynamic_allocation_3_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_rlc_entity_2', obj=rlc_entity_struct),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='uplink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_1', obj=additional_pfcs_struct)]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_2', obj=additional_pfcs_struct)]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_3', obj=additional_pfcs_struct)]),
    CSN1Val(name='', val='0')])}),
  CSN1Bit(name='primary_tsc_set')]),
  '11': ('', [
  CSN1Bit(bit=-1)])})

carrier_specific_info_struct = CSN1Alt(name='carrier_specific_info_struct', alt={
  '00': ('', []),
  '01': ('', []),
  '10': ('', [
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='timeslot_allocation', bit=8)])})]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='downlink_pdch_pairs_dlmc', bit=8),
      CSN1Bit(name='rtti_downlink_pdch_pair_assignment_dlmc', bit=4)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='maio', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0', bit=4),
    CSN1Bit(name='pr_mode')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='downlink_tfi_assignment', bit=5),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='downlink_etfi_assignment', bit=3)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='power_control_parameters', obj=power_control_parameters_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='rlc_entity_2', obj=rlc_entity_struct),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='downlink_etfi_assignment', bit=3)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='rlc_entity_3', obj=rlc_entity_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='downlink_etfi_assignment', bit=3)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_1', obj=additional_pfcs_struct),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='downlink_etfi_assignment', bit=3)])})]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_2', obj=additional_pfcs_struct),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='downlink_etfi_assignment', bit=3)])})]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='emsr_additional_pfcs_3', obj=additional_pfcs_struct),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='downlink_etfi_assignment', bit=3)])})]),
    CSN1Val(name='', val='0')])}),
  CSN1Bit(name='primary_tsc_set'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='secondary_dl_tsc_set'),
    CSN1Bit(name='secondary_dl_tsc_value', bit=3)])})]),
  '11': ('', [
  CSN1Bit(bit=-1)])})

ufps_struct = CSN1Alt(name='ufps_struct', alt={
  '00': ('', []),
  '01': ('', []),
  '10': ('', [
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='dlmc_frequency_parameters', obj=dlmc_frequency_parameters_ie)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='carrier_specific_info', obj=carrier_specific_info_struct)]),
  CSN1Val(name='', val='0')]),
  '11': ('', [
  CSN1Bit(bit=-1)])})

ps_handover_radio_resources_3_ie = CSN1List(name='ps_handover_radio_resources_3_ie', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='handover_reference', bit=8)])}),
  CSN1Bit(name='si', bit=2),
  CSN1Bit(name='nci'),
  CSN1Bit(name='bsic', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ccn_active')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_3g_ccn_active')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ccn_support_description', obj=ccn_support_description_struct)])}),
  CSN1List(list=[
    CSN1Bit(name='downlink_rlc_mode'),
    CSN1Bit(name='control_ack'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='ufps', obj=ufps_struct)]),
    CSN1Val(name='', val='0'),
    CSN1Bit(name='dlmc_measurement_type'),
    CSN1Bit(name='link_quality_measurement_mode', bit=2),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='carrier_for_interference_measurements', bit=4)])}),
    CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='ptcch_carrier', bit=4)])}),
    CSN1Bit(name='pdan_coding'),
    CSN1Bit(name='extended_sns'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bep_period2', bit=4)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi_of_downlink_tbf', bit=7)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='downlink_npm_transfer_time', bit=5)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='event_based_fanr')])}),
    CSN1Ref(name='downlink_egprs_level', obj=egprs_level_ie),
    CSN1Bit(name='indication_of_upper_layer_pdu_start_for_rlc_um'),
    CSN1Bit(name='egprs_packet_downlink_ack_nack_type_3_support'),
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)]),
  CSN1List(list=[
    CSN1Bit(name='resegment'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='dlmc_ul_carrier_info', obj=dlmc_ul_carrier_info_struct)]),
    CSN1Val(name='', val='0'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
    CSN1Bit(name='uplink_tfi_assignment', bit=5),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi_of_uplink_tbf', bit=7)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='uplink_rlc_mode')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='uplink_npm_transfer_time', bit=5)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='reported_timeslots', bit=8),
        CSN1Bit(name='tsh', bit=2)])})])}),
    CSN1Ref(name='uplink_egprs_level', obj=egprs_level_ie),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='pulse_format', obj=pulse_format_ie)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='uplink_control_timeslot', bit=3)])})]),
  CSN1Bit(name='network_control_order', bit=2),
  CSN1Bit(name='rlc_reset')])

